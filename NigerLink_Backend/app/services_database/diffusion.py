from typing import List

from app.models.chaine import Chaine
from app.models.diffusion import Diffusion
from app.models.user import User
from app.schemas.diffusion import CreateDiffusionModel, ResponseGetDiffusion
from app.schemas.success import ResponseSuccess
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime


def createDiffusion(diffusion: CreateDiffusionModel, userId: int, db: Session):
    chaine = db.scalar(select(Chaine).where(Chaine.chaineId == diffusion.chaineId))
    if chaine is None:
        raise HTTPException(
            status_code=404,
            detail="Chaine non trouvee"
        )
    
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouve"
        )
    if chaine.gestionnaireId != userId and user.role.titre != "superAdmin":
            raise HTTPException(
                status_code=403,
                detail="Aucune autorisation"
            )
            
    neWdiffusion = Diffusion(
        titre = diffusion.titre,
        description = diffusion.description,
        chaineId = chaine.chaineId,
        video = diffusion.video,
        diffusedByNom = user.nom + " " + user.prenom,
        motCle = diffusion.motCle,
    )
    
    db.add(neWdiffusion)
    db.commit()
    db.refresh(neWdiffusion)
    return ResponseGetDiffusion(
        diffusionId=neWdiffusion.diffusionId,
        titre=neWdiffusion.titre,
        description=neWdiffusion.description,
        chaineId=neWdiffusion.chaineId,
        video=neWdiffusion.video,
        diffusedByNom=neWdiffusion.diffusedByNom,
        nbCommentaire=neWdiffusion.nbCommentaire,
        nbLIke=neWdiffusion.nbLike,
        motCle=neWdiffusion.motCle,
        dateCreate=neWdiffusion.dateCreate
    )

def deleteDiffusion(diffusionId: int, chaineId: int, userId: int, db: Session):
    diffusion = db.scalar(select(Diffusion).where(Diffusion.diffusionId == diffusionId))
    if diffusion is None:
        raise HTTPException(
            status_code=404,
            detail="Diffusion non trouve"
        )
    chaine = db.scalar(select(Chaine).where(Chaine.chaineId == chaineId))
    if chaine is None:
        raise HTTPException(
            status_code=400,
            detail="Chaine non trouvee"
        )
    if  diffusion.chaineId != chaine.chaineId:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User non trouve"
        )
    if user.userId != chaine.gestionnaireId and user.role.titre not in ["superAdmin", "admin"]:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    
    db.delete(diffusion)
    db.commit()
    return ResponseSuccess(
        message="Diffusion supprime avec succes",
        status="ok",
        id=diffusion.diffusionId
    )
    
def getDiffusions(db: Session) -> List[ResponseGetDiffusion]:
    diffusions = db.scalars(select(Diffusion)).all()
    return [
        ResponseGetDiffusion(
            diffusionId= diffusion.diffusionId,
            titre=diffusion.titre,
            description=diffusion.description,
            chaineId=diffusion.chaineId,
            video=diffusion.video,
            diffusedByNom=diffusion.diffusedByNom,
            nbCommentaire=diffusion.nbCommentaire,
            nbLIke=diffusion.nbLike,
            motCle=diffusion.motCle,
            dateCreate=diffusion.dateCreate   
        ) for diffusion in diffusions
    ]
   
    
