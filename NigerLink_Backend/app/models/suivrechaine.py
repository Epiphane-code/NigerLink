from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class SuivreChaine(BaseAlchemy):
    __tablename__ = "suivrechaines"
    suivrechaineId: Mapped[int] = mapped_column(primary_key = True, index = True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    chaineId: Mapped[int] = mapped_column(ForeignKey("chaines.chaineId"))