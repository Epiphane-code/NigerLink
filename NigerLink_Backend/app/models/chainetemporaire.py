from sqlalchemy import String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy
from datetime import datetime

class ChaineTemporaire(BaseAlchemy):
    __tablename__ = "chainestemporaires"
    chaineId: Mapped[int] = mapped_column(primary_key = True, index = True)
    titre: Mapped[str] = mapped_column(String(100))
    pays: Mapped[str] = mapped_column(String(250))
    ville: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))
    followers: Mapped[int] = mapped_column(Integer, default=0)
    motCle: Mapped[str] = mapped_column(String(250))
    gestionnaireId: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    createById: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    statut: Mapped[str] = mapped_column(String(20), default="encours")