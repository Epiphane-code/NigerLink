from app.schemas.base import SchemaModel
from datetime import datetime

class CreateDiffusionModel(SchemaModel):
    titre: str
    description: str
    chaineId: int
    video: str
    motCle: str
    
class ResponseGetDiffusion(SchemaModel):
    diffusionId: int
    titre: str
    description: str
    chaineId: int
    video: str
    diffusedByNom: str
    nbCommentaire: int
    nbLIke: int
    motCle: str
    dateCreate: datetime