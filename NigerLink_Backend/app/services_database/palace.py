from sqlalchemy import select, and_, or_, delete
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app.schemas.palace import PalaceCreate
from app.models.palacetemporaire import PalaceTemporaire
from app.models.palace import Palace
from app.models.user import User
from app.models.role import Role
from app.schemas.palace import ResponseGetPalace


def palaceToBase(id: int, palace: PalaceCreate, db: Session) -> ResponseGetPalace:

    # Rechercher l'utilisateur qui crée le palace
    user = db.scalar(
        select(User).where(User.userId == id)
    )

    # Vérifier si un palace avec le même titre
    # et la même catégorie existe déjà
    newPalace = db.scalar(
        select(Palace).where(
            and_(
                Palace.titre == palace.titre,
                Palace.categorie == palace.categorie
            )
        )
    )

    if newPalace is not None:
        raise HTTPException(
            status_code=409,
            detail="Un nom similaire de la même catégorie existe déjà."
        )

    # Vérifier que l'utilisateur existe
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé."
        )

    # Vérifier le rôle de l'utilisateur
    userrole = db.scalar(select(Role).where(Role.roleId == user.roleId))
    if userrole.titre in ["citoyen", "admin", "superAdmin"]:

        newPalace = PalaceTemporaire(
            titre=palace.titre,
            categorie=palace.categorie,
            description=palace.description,
            latitude=palace.latitude,
            longitude=palace.longitude,
            motCle=palace.motCle,
            image=palace.image,
            createById=user.userId,
            createByNom=user.nom + " " + user.prenom,
            dateCreate=datetime.now()
        )

    else:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation."
        )

    # Enregistrer dans la base
    db.add(newPalace)
    db.commit()
    db.refresh(newPalace)

    return ResponseGetPalace(
                palaceId=palace.palaceId,
                titre=palace.titre,
                categorie=palace.categorie,
                description=palace.description,
                latitude=palace.latitude,
                longitude=palace.longitude,
                motCle=palace.motCle,
                image=palace.image,
                createById=palace.createById,
                createByNom=palace.createByNom,
                dateCreate=palace.dateCreate,
                approvedById=None,
                approvedByNom=None,
                dateApproved=None
                )

def validerPalace(palaceId: int, userId: int, db: Session) -> ResponseGetPalace:

    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé"
        )

    roleUser = db.scalar(
        select(Role).where(Role.roleId == user.roleId)
    )

    if roleUser is None:
        raise HTTPException(
            status_code=403,
            detail="Rôle utilisateur introuvable"
        )

    if roleUser.titre not in ["admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Vous n'avez pas les permissions nécessaires"
        )

    palacetemp = db.scalar(
        select(PalaceTemporaire)
        .where(PalaceTemporaire.palaceId == palaceId)
    )

    if palacetemp is None:
        raise HTTPException(
            status_code=404,
            detail="Palace temporaire introuvable"
        )

    palaceNew = Palace(
        titre=palacetemp.titre,
        categorie=palacetemp.categorie,
        description=palacetemp.description,
        latitude=palacetemp.latitude,
        longitude=palacetemp.longitude,
        motCle=palacetemp.motCle,
        image=palacetemp.image,
        createById=palacetemp.createById,
        createByNom=palacetemp.createByNom,
        dateCreate=palacetemp.dateCreate,
        approvedByNom=user.nom + " " + user.prenom,
        dateApproved=datetime.now()
    )

    # Ajouter le nouveau palace
    db.add(palaceNew)

    # Supprimer le palace temporaire
    db.delete(palacetemp)

    # Appliquer les deux opérations
    db.commit()

    # Récupérer le Palace créé avec son ID
    db.refresh(palaceNew)

    return  ResponseGetPalace(
                palaceId=palaceNew.palaceId,
                titre=palaceNew.titre,
                categorie=palaceNew.categorie,
                description=palaceNew.description,
                latitude=palaceNew.latitude,
                longitude=palaceNew.longitude,
                motCle=palaceNew.motCle,
                image=palaceNew.image,
                createById=palaceNew.createById,
                createByNom=palaceNew.createByNom,
                dateCreate=palaceNew.dateCreate,
                approvedById=palaceNew.approvedById,
                approvedByNom=palaceNew.approvedByNom,
                dateApproved=palaceNew.dateApproved
                )
    


def getPalaceTemp(userId: int, db: Session) -> List[ResponseGetPalace]:

    # Rechercher l'utilisateur
    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé."
        )

    # Vérifier son rôle
    if user.role.titre not in ["admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Vous n'avez pas l'autorisation."
        )

    # Récupérer les palaces temporaires
    palaces = db.scalars(
        select(PalaceTemporaire)
    ).all()

    return [
        ResponseGetPalace(
            palaceId=palace.palaceId,
            titre=palace.titre,
            categorie=palace.categorie,
            description=palace.description,
            latitude=palace.latitude,
            longitude=palace.longitude,
            motCle=palace.motCle,
            image=palace.image,
            createById=palace.createById,
            createByNom=palace.createByNom,
            dateCreate=palace.dateCreate,
            approvedById=None,
            approvedByNom=None,
            dateApproved=None
            ) for palace in palaces
    ]



def getPalace(db: Session) -> ResponseGetPalace:

    # Récupérer les palaces temporaires
    palaces = db.scalars(
        select(Palace)
    ).all()

    return [
            ResponseGetPalace(
                palaceId=palace.palaceId,
                titre=palace.titre,
                categorie=palace.categorie,
                description=palace.description,
                latitude=palace.latitude,
                longitude=palace.longitude,
                motCle=palace.motCle,
                image=palace.image,
                createById=palace.createById,
                createByNom=palace.createByNom,
                dateCreate=palace.dateCreate,
                approvedById=palace.approvedById,
                approvedByNom=palace.approvedByNom,
                dateApproved=palace.dateApproved
                ) for palace in palaces
        ]

def deleteAllPalaceTemp(userId: int, db: Session):

    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="user non trouve"
        )

    if user.role is None or user.role.titre != "superAdmin":
        raise HTTPException(
            status_code=403,
            detail="vous n'etes pas autorise"
        )

    result = db.execute(
        delete(PalaceTemporaire)
    )

    db.commit()

    return {
        "message": "Tous les palais temporaires ont été supprimés",
        "nombre_supprime": result.rowcount
    }
    
def deletePalace(userId: int, palaceId: int, db: Session):

    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé"
        )

    if user.role is None or user.role.titre not in ["superAdmin", "admin"]:
        raise HTTPException(
            status_code=403,
            detail="Vous n'êtes pas autorisé"
        )

    palace = db.scalar( select(Palace).where(Palace.palaceId == palaceId) )

    if palace is None:
        raise HTTPException(
            status_code=404,
            detail="Palace non trouvé"
        )

    if (
        user.role.titre == "admin"
        and palace.approvedById != user.userId
    ):
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )

    try:
        db.delete(palace)
        db.commit()

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la suppression du lieu"
        )

    return {
        "message": "Le lieu a été supprimé"
    }