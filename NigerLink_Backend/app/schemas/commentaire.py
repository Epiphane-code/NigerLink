from app.schemas.base import SchemaModel
from enum import Enum
from datetime import datetime

class TypeComment(str, Enum):
    diffusion = "diffusion"
    commentaire = "commentaire"
    
class CommentaireCreate(SchemaModel):
    type: TypeComment
    objetId: int
    value: str
    
    
class ResponseGetCommentaires(SchemaModel):
    commentaireId: int
    type: TypeComment
    objetId: int
    nbCommentaire: int
    nbLike: int
    createById: int
    dateCreate: datetime
    createByNom: str
    value: str