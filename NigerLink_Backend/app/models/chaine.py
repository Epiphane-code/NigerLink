from sqlalchemy import String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy
from datetime import datetime

class Chaine(BaseAlchemy):
    __tablename__ = "chaines"
    chaineId: Mapped[int] = mapped_column(primary_key = True, index = True)
    titre: Mapped[str] = mapped_column(String(250))
    pays: Mapped[str] = mapped_column(String(250))
    ville: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))
    followers: Mapped[int] = mapped_column(Integer, default=0)
    motCle: Mapped[str] = mapped_column(String(250), nullable=True)
    gestionnaireId: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    createById: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    dateCreate: Mapped[datetime] = mapped_column(DateTime)
    approvedById: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    approvedByNom: Mapped[str] = mapped_column(String(250))
    dateApproved: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())