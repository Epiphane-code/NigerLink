from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseAlchemy

class DiscussionBot(BaseAlchemy):
    __tablename__ = "discussionsbots"
    chatId: Mapped[int] = mapped_column(primary_key = True, index = True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.userId"))