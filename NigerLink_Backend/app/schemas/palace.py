from app.schemas.base import SchemaModel
from datetime import datetime

class PalaceCreate(SchemaModel):
    titre: str
    categorie: str
    description: str
    latitude: str
    longitude: str
    motCle: str
    image: str
    
class ResponseGetPalace(SchemaModel):
    palaceId: int
    titre: str
    categorie: str
    description: str
    latitude: str
    longitude: str
    motCle: str | None
    image: str | None
    createById: int
    createByNom: str
    dateCreate: datetime
    approvedById: int | None
    approvedByNom: str | None
    dateApproved: datetime | None