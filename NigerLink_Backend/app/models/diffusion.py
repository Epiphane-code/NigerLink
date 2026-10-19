from datetime import datetime

from sqlalchemy import String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseAlchemy


class Diffusion(BaseAlchemy):
    __tablename__ = "diffusions"

    diffusionId: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    titre: Mapped[str] = mapped_column(
        String(100)
    )

    description: Mapped[str] = mapped_column(
        String(250)
    )

    chaineId: Mapped[int] = mapped_column(
        ForeignKey("chaines.chaineId")
    )

    video: Mapped[str] = mapped_column(
        String(250)
    )

    diffusedByNom: Mapped[str] = mapped_column(
        String(100)
    )

    nbCommentaire: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    nbLike: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    motCle: Mapped[str] = mapped_column(
        String(250)
    )

    dateCreate: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )