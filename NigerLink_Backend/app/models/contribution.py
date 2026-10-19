from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class Contribution(BaseAlchemy):
    __tablename__ = "contributions"
    contributionId: Mapped[int] = mapped_column(primary_key = True, index = True)
    userId: Mapped[int] = mapped_column(primary_key = True, index = True)
    lieuCategorie: Mapped[str] = mapped_column(String(50))
    lieuId: Mapped[int] = mapped_column(Integer)
    aprouved: Mapped[bool] = mapped_column(Boolean, default = False)
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)