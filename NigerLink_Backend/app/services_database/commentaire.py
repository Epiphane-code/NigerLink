
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from app.models.commentaire import Commentaire
from app.models.diffusion import Diffusion
from app.models.user import User
from app.schemas.success import ResponseSuccess
from app.schemas.commentaire import (
    CommentaireCreate,
    ResponseGetCommentaires,
    TypeComment,
)


def createCommentaire(
    commentaireData: CommentaireCreate,
    userId: int,
    db: Session,
):
    # 1. Vérifier l'utilisateur
    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé",
        )

    # 2. Vérifier les autorisations
    if user.role.titre not in ["citoyen", "admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation",
        )

    # 3. Déterminer la cible du commentaire
    if commentaireData.type == TypeComment.diffusion:
        cible = db.scalar(
            select(Diffusion).where(
                Diffusion.diffusionId == commentaireData.objetId
            )
        )

        if cible is None:
            raise HTTPException(
                status_code=404,
                detail="Diffusion non trouvée",
            )

    elif commentaireData.type == TypeComment.commentaire:
        cible = db.scalar(
            select(Commentaire).where(
                Commentaire.commentaireId == commentaireData.objetId
            )
        )

        if cible is None:
            raise HTTPException(
                status_code=404,
                detail="Commentaire parent non trouvé",
            )

    else:
        raise HTTPException(
            status_code=400,
            detail="Type de commentaire invalide",
        )

    # 4. Construire le commentaire
    commentaire = Commentaire(
        type=commentaireData.type.value,
        objetId=commentaireData.objetId,
        nbCommentaire=0,
        nbLike=0,
        createById=userId,
        dateCreate=datetime.now(),
        createByNom=f"{user.nom} {user.prenom}",
        value=commentaireData.value,
    )

    # 5. Enregistrer en base
    try:
        db.add(commentaire)
        db.commit()
        db.refresh(commentaire)

    except Exception:
        db.rollback()
        raise

    # 6. Retourner la réponse
    return ResponseGetCommentaires(
        commentaireId=commentaire.commentaireId,
        type=commentaire.type,
        objetId=commentaire.objetId,
        nbCommentaire=commentaire.nbCommentaire,
        nbLike=commentaire.nbLike,
        createById=commentaire.createById,
        dateCreate=commentaire.dateCreate,
        createByNom=commentaire.createByNom,
        value=commentaire.value,
    )
def getCommentairesDiffusion(diffusionId: int, db: Session):
    diffusion = db.scalar(select(Diffusion).where(Diffusion.diffusionId == diffusionId))
    if diffusion is None:
        raise HTTPException(
            status_code=404,
            detail="diffusion non trouve"
        )
    commentaires = db.scalars(select(Commentaire).where(and_(Commentaire.objetId == diffusionId, Commentaire.type == TypeComment.diffusion))).all()
    if commentaires is None:
        raise HTTPException(
            status_code=404,
            detail="Commentaire non trouve"
        )
    return [ResponseGetCommentaires(
        commentaireId=commentaire.commentaireId,
        type=commentaire.type,
        objetId=commentaire.objetId,
        nbCommentaire=commentaire.nbCommentaire,
        nbLike=commentaire.nbLike,
        createById=commentaire.createById,
        dateCreate=commentaire.dateCreate,
        createByNom=commentaire.createByNom,
        value=commentaire.value
    ) for commentaire in commentaires
    ]
def getSousCommentaire(commentairePrincipaleId: int, db: Session):
    commentaireP = db.scalar(select(Commentaire).where(Commentaire.commentaireId == commentairePrincipaleId))
    if commentaireP is None:
        raise HTTPException(
            status_code=404,
            detail="Commentaire Principale non trouve"
        )
    commentaires = db.scalars(select(Commentaire).where(and_(Commentaire.type == TypeComment.commentaire, Commentaire.objetId == commentairePrincipaleId)))
    if commentaires is None:
        raise HTTPException(
            status_code=404,
            detail="Commentaires non trouves"
        )
    return [ResponseGetCommentaires(
            commentaireId=commentaire.commentaireId,
            type=commentaire.type,
            objetId=commentaire.objetId,
            nbCommentaire=commentaire.nbCommentaire,
            nbLike=commentaire.nbLike,
            createById=commentaire.createById,
            dateCreate=commentaire.dateCreate,
            createByNom=commentaire.createByNom,
            value=commentaire.value
        ) for commentaire in commentaires
        ]
    
def deleteCommentaire(commentaireId: int,userId: int, db: Session):
    commentaire = db.scalar(select(Commentaire).where(Commentaire.commentaireId == commentaireId))
    if commentaire is None:
        raise HTTPException(
            status_code=404,
            detail="Commentaire non trouve"
        )
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouve"
        )
    if commentaire.createById != user.userId and user.role.titre != "superAdmin":
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )
    db.delete(commentaire)
    db.commit()
    return ResponseSuccess(
        message="commentaire supprime",
        status="ok",
        id=commentaire.commentaireId
    )