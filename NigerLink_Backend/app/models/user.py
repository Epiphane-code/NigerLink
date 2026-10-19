from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.role import Role

from app.models.base import BaseAlchemy


class User(BaseAlchemy):
    __tablename__ = "users"

    userId: Mapped[int] = mapped_column(primary_key=True, index=True)

    nom: Mapped[str] = mapped_column(String(100))
    
    prenom: Mapped[str] = mapped_column(String(100))
    
    pays: Mapped[str] = mapped_column(String(100), nullable=True)
    
    ville: Mapped[str] = mapped_column(String(100), nullable=True)
    
    quartier: Mapped[str] = mapped_column(String(100), nullable=True)

    email: Mapped[str] = mapped_column( String(255), nullable=True, index=True,)
    
    proffession: Mapped[str] = mapped_column(String(100))
    
    nationnalite: Mapped[str] = mapped_column(String(100))
    
    sexe: Mapped[str] = mapped_column(String(100))
    
    photo: Mapped[str] = mapped_column(String(250), nullable=True)

    phone: Mapped[str] = mapped_column( String(100), unique=True,)
    
    deviceIdentifiant: Mapped[str] = mapped_column(String(250),)
    
    deviceName: Mapped[str] = mapped_column(String(100),) 

    password: Mapped[str] = mapped_column(String(255))

    roleId: Mapped[int] = mapped_column(ForeignKey("roles.roleId"))
    
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    
    role: Mapped["Role"] = relationship(
                "Role",
                back_populates="users"
            )