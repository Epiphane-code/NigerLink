from sqlalchemy import select

from app.database.database import SessionLocal
from app.models.role import Role
from app.models.user import User
from app.core.security import hash_password
from app.seed.palacesData import palaces
from app.models.palacetemporaire import PalaceTemporaire
from datetime import datetime


def create_roles():
    with SessionLocal() as db:

        # =========================
        # Création du rôle visiteur
        # =========================

        role = db.scalar(
            select(Role).where(Role.titre == "visiteur")
        )

        if role is None:
            role = Role(
                titre="visiteur",
                description="Utilisateur visiteur"
            )

            db.add(role)
            db.commit()
            db.refresh(role)

            print("Rôle visiteur créé.")

        else:
            print("Rôle visiteur existe déjà.")
            print(role.roleId)
        
        
        
        role = db.scalar(
            select(Role).where(Role.titre == "citoyen")
        )

        if role is None:
            role = Role(
                titre="citoyen",
                description="Utilisateur citoyen"
            )

            db.add(role)
            db.commit()
            db.refresh(role)

            print("Rôle citoyen créé.")

        else:
            print("Rôle citoyen existe déjà.")
            print(role.roleId)
            
        
        role = db.scalar(
            select(Role).where(Role.titre == "admin")
        )

        if role is None:
            role = Role(
                titre="admin",
                description="Utilisateur admin"
            )

            db.add(role)
            db.commit()
            db.refresh(role)

            print("Rôle admin créé.")

        else:
            print("Rôle admin existe déjà.")
            print(role.roleId)
            
        
        role = db.scalar(
            select(Role).where(Role.titre == "superAdmin")
        )

        if role is None:
            role = Role(
                titre="superAdmin",
                description="Utilisateur superAdmin"
            )

            db.add(role)
            db.commit()
            db.refresh(role)

            print("Rôle superAdmin créé.")

        else:
            print("Rôle superAdmin existe déjà.")
            print(role.roleId)




        # =========================
        # Création du compte visiteur
        # =========================

                
        visiteur_role = db.scalar(
            select(Role).where(Role.titre == "visiteur")
        )

        user = db.scalar(
            select(User).where(User.role == visiteur_role)
        )

        if user is None:

            user = User(
                nom="visiteur",
                prenom="account",
                email="exemple@gmail.com",
                proffession="Profession",
                nationnalite="Nationalité",
                sexe="Sexe",
                phone="227 xxxxxxxx",
                deviceIdentifiant="Device Id",
                deviceName="DeviceName",
                password=hash_password("1234"),
                role=visiteur_role,
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            print("Utilisateur visiteur créé.")

        else:
            print("Utilisateur existe déjà.")
            print(user.nom)
        
        
                
        visiteur_role = db.scalar(
                    select(Role).where(Role.titre == "superAdmin")
                )
        
        user = db.scalar(
                    select(User).where(User.role == visiteur_role)
                )
        
        if user is None:
        
            user = User(
                        nom="superAdmin",
                        prenom="account",
                        email="superAdmin@gmail.com",
                        proffession="Profession",
                        nationnalite="Nationalité",
                        sexe="Sexe",
                        phone="superAdmin",
                        deviceIdentifiant="Device Id",
                        deviceName="DeviceName",
                        password=hash_password("1234"),
                        role=visiteur_role,
                    )
        
            db.add(user)
            db.commit()
            db.refresh(user)
        
            print("Utilisateur super admin créé.")
        
        else:
            print("Utilisateur existe déjà.")
            print(user.nom)
            
            
        
        
        for data in palaces:

            palace = PalaceTemporaire(
            titre=data["titre"],
            categorie=data["categorie"],
            description=data["description"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            motCle=data["motCle"],
            image=data["image"],
            createById=user.userId,
            createByNom=user.nom + " " + user.prenom,
            dateCreate=datetime.now()
            )

            db.add(palace)

        db.commit()
            
        
                    
            


if __name__ == "__main__":
    create_roles()