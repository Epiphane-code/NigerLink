from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import delete, select
from fastapi import HTTPException
from datetime import datetime

from app.models.chaine import Chaine
from app.models.chainetemporaire import ChaineTemporaire
from app.models.role import Role
from app.models.user import User
from app.schemas.chaine import ChaineCreateModel, ResponseGetChaine
from app.schemas.success import ResponseSuccess, Status
def createChaine(chaine: ChaineCreateModel, userId: int, db: Session) -> ResponseSuccess:
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="utilisateur non trouve"
        )
    if user.role.titre not in ["citoyen", "admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="aucune autorisation"
        )
    newChaine = ChaineTemporaire(
        titre=chaine.titre,
        pays=chaine.pays,
        ville= chaine.ville,
        description = chaine.description,
        motCle=chaine.motCle,
        gestionnaireId = user.userId,
        createById = user.userId,
        dateCreate = datetime.now() 
    )
    
    db.add(newChaine)
    db.commit()
    db.refresh(newChaine)
    
    return ResponseSuccess(
        message="Creation d'une nouvelle chaine encours, cette chaine sera visible, une fois approuvee par un admin",
        status=Status.success,
        id=newChaine.chaineId
    )
    
def validerChaine(chaineId: int, userId: int, db: Session):
    chaine = db.scalar(select(ChaineTemporaire).where(ChaineTemporaire.chaineId == chaineId))
    if chaine is None:
        raise HTTPException(
            status_code=404,
            detail="Chaine non trouvee"
        )
    user = db.scalar(select(User).where(User.userId == userId))
    if user is  None:
        raise HTTPException(
                    status_code=404,
                    detail="Utilisateur non trouve"
                )
    if user.role.titre not in ["admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    newChaine = Chaine(
        titre = chaine.titre,
        pays = chaine.pays,
        ville = chaine.ville,
        description = chaine.description,
        motCle = chaine.motCle,
        gestionnaireId = chaine.gestionnaireId,
        createById = chaine.createById,
        dateCreate = chaine.dateCreate,
        approvedById = userId,
        approvedByNom = user.nom + " " + user.prenom,
        dateApproved = datetime.now()
    )
    db.delete(chaine)
    db.add(newChaine)
    db.commit()
    db.refresh(newChaine)
    return ResponseGetChaine(
        chaineId=newChaine.chaineId,
        titre=newChaine.titre,
        pays=newChaine.pays,
        ville=newChaine.ville,
        description=newChaine.description,
        followers=newChaine.followers,
        motCle=newChaine.motCle,
        gestionnaireId=newChaine.gestionnaireId,
        createById=newChaine.createById,
        dateCreate=newChaine.dateCreate,
        approvedId=newChaine.approvedById,
        approvedNom=newChaine.approvedByNom,
        dateApproved=newChaine.dateApproved
    )
    
def getChaines(db: Session) -> List[ResponseGetChaine]:
    chaines = db.scalars(select(Chaine)).all()
    if chaines is None:
        raise HTTPException(
            status_code=404,
            detail="non trouvees"
        )
    return [
        ResponseGetChaine(
        chaineId=chaine.chaineId,
        titre=chaine.titre,
        pays=chaine.pays,
        ville=chaine.ville,
        description=chaine.description,
        followers=chaine.followers,
        motCle=chaine.motCle,
        gestionnaireId=chaine.gestionnaireId,
        createById=chaine.createById,
        dateCreate=chaine.dateCreate,
        approvedId=chaine.approvedById,
        approvedNom=chaine.approvedByNom,
        dateApproved=chaine.dateApproved
    ) for chaine in chaines   
    ]
    
def deleteChaine(chaineId: int, userId: int, db: Session):
    chaine = db.scalar(select(Chaine).where(Chaine.chaineId == chaineId))
    if chaine is None:
        raise HTTPException(
            status_code=404,
            detail="Chaine non trouvee"
        )
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvee"
        )
    if user.userId != chaine.createById and user.role.titre != "superAdmin":
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    try:
        db.delete(chaine)
        db.commit()
    except Exception:
        db.rollback
        raise HTTPException(
            status_code=500,
            detail="Erreur de la suppression"        
            )
    return ResponseSuccess(
        message="Chaine supprimee avec succes",
        status="ok",
        id=None
    )
    
def deleteAllChaineTemporaires(userId:int, db: Session) -> ResponseSuccess:
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouve"
        )
    if user.role.titre != "superAdmin":
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    resultat = db.execute(
        delete(ChaineTemporaire)
    )
    
    db.commit()
    
    if resultat.rowcount == 0:
        raise HTTPException(
                    status_code=404,
                    detail="Aucune chaine temporaire"
                )
    
    return ResponseSuccess(
        message="vous avez supprimer toutes les Chaines temporaires",
        status="ok",
        id=None
    )
    
def deleteChaine(chaineId: int, userId: int, db: Session):
    chaine = db.scalar(select(Chaine).where(Chaine.chaineId == chaineId))
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
    if userId != chaine.createById and user.role.titre != "superAdmin":
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    db.delete(chaine)
    db.commit()
    return ResponseSuccess(
            message="vous avez supprimer la chaine:",
            status="ok",
            id= chaine.chaineId
        )
    
    
    
        

    
        
    