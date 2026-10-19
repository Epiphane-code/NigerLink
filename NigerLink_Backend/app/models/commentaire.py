from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class Commentaire(BaseAlchemy):
    __tablename__ = "commentaires"
    commentaireId: Mapped[int] = mapped_column(primary_key = True, index = True)
    type: Mapped[str] = mapped_column(String(20))
    objetId: Mapped[int] = mapped_column(Integer)
    nbCommentaire: Mapped[int] = mapped_column(Integer, default = 0)
    nbLike: Mapped[int] = mapped_column(Integer, default = 0)
    createById: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    createByNom: Mapped[str] = mapped_column(String(100))
    value: Mapped[str] = mapped_column(Text)
    