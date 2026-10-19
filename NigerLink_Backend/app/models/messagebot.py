from datetime import datetime
from sqlalchemy import String, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.models.base import BaseAlchemy

class MessageBot(BaseAlchemy):
    __tablename__ = "messagesbots"
    messagebotId: Mapped[int] = mapped_column(primary_key = True, index = True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.userId"))
    isEmetteur: Mapped[bool] = mapped_column(Boolean, nullable = False)
    content: Mapped[str] = mapped_column(Text, nullable =  False)
    isUpdate: Mapped[bool] = mapped_column(Boolean, default = False)
    dateCreate: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    