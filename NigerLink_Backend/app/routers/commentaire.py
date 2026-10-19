from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.commentaire import ResponseGetCommentaires, CommentaireCreate
from app.schemas.success import ResponseSuccess
from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.services_database.commentaire import createCommentaire, getCommentairesDiffusion, getSousCommentaire, deleteCommentaire

router = APIRouter(
    prefix="/commentaire",
    tags=["Private"]
)

@router.post("/commenter", response_model=ResponseGetCommentaires)
def Commenter(commentaire: CommentaireCreate, token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    userId = int(token["sub"])
    return createCommentaire(commentaireData=commentaire, userId=userId, db=db)
@router.delete("/deleteCommentaire", response_model=ResponseSuccess)
def DeleteCommentaire(commentaireId: int, token: dict=Depends(get_current_user), db: Session=Depends(get_db)):
    userId = int(token["sub"])
    return deleteCommentaire(commentaireId=commentaireId, userId=userId, db=db)

routerPublic = APIRouter(
    prefix="/commentaire",
    tags=["Public"]
    
)

@routerPublic.get("/getCommentaireDiffusion", response_model=List[ResponseGetCommentaires])
def GetCommentaireDiffusion(diffusionId:int, db:Session = Depends(get_db)):
    return getCommentairesDiffusion(diffusionId=diffusionId, db=db)

@routerPublic.get("/getSousCommentaire", response_model=List[ResponseGetCommentaires])
def GetSousCommentaire(commentairePincipaleId:int, db:Session = Depends(get_db)):
    return getSousCommentaire(commentairePrincipaleId=commentairePincipaleId, db=db)