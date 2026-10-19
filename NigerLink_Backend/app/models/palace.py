from datetime import datetime
from sqlalchemy import Boolean, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class Palace(BaseAlchemy):
    __tablename__ = "palaces"
    palaceId: Mapped[int] = mapped_column(primary_key = True, index = True)
    titre: Mapped[str] = mapped_column(String(250))
    categorie: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(Text)
    horaire: Mapped[str] = mapped_column(String(250), nullable= True)
    isGarde: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    phone: Mapped[str] = mapped_column(String(250), nullable=True)
    latitude: Mapped[str] = mapped_column(String(250))
    longitude: Mapped[str] = mapped_column(String(250))
    motCle: Mapped[str] = mapped_column(String(250))
    image: Mapped[str] = mapped_column(String(250))
    createById: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    createByNom: Mapped[str] = mapped_column(String(250))
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    approvedById: Mapped[int] = mapped_column(ForeignKey("users.userId"), nullable=True)
    approvedByNom: Mapped[str] = mapped_column(String(250))
    dateApproved: Mapped[datetime] = mapped_column(DateTime, default= datetime.now())
    