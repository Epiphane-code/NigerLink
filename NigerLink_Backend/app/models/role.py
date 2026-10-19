from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import BaseAlchemy



class Role(BaseAlchemy):
    __tablename__ = "roles"
    roleId: Mapped[int] = mapped_column(primary_key=True, index=True )
    titre: Mapped[str] = mapped_column(String(50), unique=True, nullable = False)
    description: Mapped[str]=mapped_column(String(100))
    users: Mapped[list["User"]] = relationship(
            "User",
            back_populates="role"
        )
    