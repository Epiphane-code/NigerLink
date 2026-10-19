from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class Urgence(BaseAlchemy):
    __tablename__ = "urgences"
    urgenceId: Mapped[int] = mapped_column(primary_key = True, index = True)
    titre: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(250))
    phone: Mapped[str] = mapped_column(String(50))