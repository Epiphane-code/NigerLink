from fastapi import HTTPException
from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.user import UserCreate, UserInfo, ResponseRestorePassword
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password
from app.schemas.success import ResponseSuccess


def userToBase(userInfo: UserCreate, db: Session) -> ResponseSuccess:

    user = db.scalar(
        select(User).where(
            or_(
                User.email == userInfo.email,
                User.phone == userInfo.phone
            )
        )
    )

    if user is not None:
        raise HTTPException(
            status_code=409,
            detail="Un compte utilise déjà cet email ou ce numéro de téléphone."
        )

    user = User(
        nom=userInfo.nom,
        prenom=userInfo.prenom,
        pays=userInfo.pays,
        ville=userInfo.ville,
        quartier=userInfo.quartier,
        email=userInfo.email,
        proffession=userInfo.proffession,
        nationnalite=userInfo.nationnalite,
        sexe=userInfo.sexe,
        photo="",
        phone=userInfo.phone,
        deviceIdentifiant=userInfo.deviceId,
        deviceName=userInfo.deviceName,
        password=userInfo.password,
        roleId=1,
        dateCreate=datetime.now()
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return ResponseSuccess(
        message="Ajout avec success",
        status="ok",
        id=user.userId
    )

def getUsers(userId: int, db: Session):
    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur non trouvé"
        )

    if user.role is None or user.role.titre not in ["admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )

    users = db.scalars(
        select(User)
    ).all()
    
    

    return [
        UserInfo(
            userId=user.userId,
            nom=user.nom,
            prenom=user.prenom,
            email=user.email,
            proffession=user.proffession,
            nationnalite=user.nationnalite,
            sexe=user.sexe,
            phone=user.phone,
            photo=user.photo,
            deviceId=user.deviceIdentifiant,
            deviceName=user.deviceName,
            role=user.role.titre,
            pays=user.pays if user.pays else None,
            ville=user.ville if user.ville else None,
            quartier=user.quartier if user.quartier else None
        )
        for user in users
       
    ]
    
def getMe(userId: int, db: Session) -> UserInfo:
    user = db.scalar(select(User).where(User.userId == userId))
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    return UserInfo(
                nom=user.nom,
                prenom=user.prenom,
                email=user.email,
                proffession=user.proffession,
                nationnalite=user.nationnalite,
                sexe=user.sexe,
                phone=user.phone,
                photo=user.photo,
                deviceId=user.deviceIdentifiant,
                deviceName=user.deviceName,
                role=user.role.titre,
                pays=user.pays,
                ville=user.ville,
                quartier=user.quartier
    )
    
def restorePassword(userId: int, adminId: int, db: Session) -> ResponseRestorePassword:

    # Vérifier l'administrateur
    admin = db.scalar(
        select(User).where(User.userId == adminId)
    )

    if not admin:
        raise HTTPException(
            status_code=404,
            detail="Administrateur introuvable"
        )

    # Vérifier son rôle
    if admin.role.titre not in ["admin", "superAdmin"]:
        raise HTTPException(
            status_code=403,
            detail="Aucune autorisation"
        )

    # Rechercher l'utilisateur à modifier
    user = db.scalar(
        select(User).where(User.userId == userId)
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable"
        )

    # Nouveau mot de passe temporaire
    new_password = "12345678"

    # Hasher le nouveau mot de passe
    user.password = hash_password(new_password)

    # Enregistrer les modifications
    db.commit()
    db.refresh(user)
    
    reponse = ResponseRestorePassword(
        message="Mot de passe réinitialisé avec succès",
        userId= user.userId,
        passewordTemporaire=new_password
    )

    return reponse

