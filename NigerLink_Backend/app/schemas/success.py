  
from app.schemas.base import SchemaModel

from enum import Enum

class Status(str, Enum):
    success = "ok"
    echec = "no"

class ResponseSuccess(SchemaModel):
    message: str
    status: Status
    id: int | None