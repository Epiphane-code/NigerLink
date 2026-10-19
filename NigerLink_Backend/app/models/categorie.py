from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy


class Categorie(BaseAlchemy):
    __tablename__ = "categories"
    categorieId: Mapped[int] = mapped_column(primary_key=True, index=True)
    titre: Mapped[str] = mapped_column(String(50),unique=True)
    description: Mapped[str] = mapped_column(String(200))
    
    