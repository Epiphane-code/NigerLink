from app.schemas.base import SchemaModel
from datetime import datetime

class ChaineCreateModel(SchemaModel):
    titre: str
    pays: str
    ville: str
    description: str
    motCle: str | None
    
class ResponseGetChaine(SchemaModel):
    chaineId: int
    titre: str
    pays: str
    ville: str
    description: str
    followers: int
    motCle: str | None
    gestionnaireId: int
    createById: int
    dateCreate: datetime
    approvedId: int | None
    approvedNom: str | None
    dateApproved: datetime | None
    