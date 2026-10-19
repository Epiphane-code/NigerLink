from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.schemas.chaine import ChaineCreateModel, ResponseGetChaine
from app.schemas.success import ResponseSuccess
from app.database.database import get_db
from app.services_database.chaine import createChaine, getChaines, validerChaine, deleteChaine, deleteAllChaineTemporaires, deleteChaine

router = APIRouter(
    prefix="/chaine",
    tags=["Private"]
)

@router.post("/ajouterChaine", response_model=ResponseSuccess)
def CreateChaine(chaine: ChaineCreateModel, token: dict=Depends(get_current_user), db: Session = Depends(get_db) ):
    userId = int(token["sub"])
    return createChaine(chaine = chaine,userId = userId, db = db)

@router.post("/validerChaine", response_model=ResponseGetChaine)
def ValiderChaine(chaineId: int, token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    userId = int(token["sub"])
    return validerChaine(chaineId=chaineId, userId=userId, db=db)

@router.delete("/deleteChaine", response_model=ResponseSuccess)
def DeleteChaine(chaineId: int, token: dict=Depends(get_current_user), db: Session=Depends(get_db)):
    userId = int(token["sub"])
    return deleteChaine(chaineId=chaineId, userId=userId, db=db)

@router.delete("/deleteChaine")
def DeleteChaine(chaineId:int, token: dict=Depends(get_current_user), db: Session=Depends(get_db)):
    userId = int(token["sub"])
    return deleteChaine(chaineId=chaineId, userId=userId, db=db)

routerPublic = APIRouter(
    prefix="/chaine",
    tags=["Public"]
)

@routerPublic.get("/getChaines", response_model=List[ResponseGetChaine])
def GetChaines(db: Session = Depends(get_db)):
    return getChaines(db=db)

routerPrivate2 = APIRouter(
    prefix="/chaine",
        tags=["Private X2"]
)

@routerPrivate2.delete("/deleteAllChainesTemporaires", response_model=ResponseSuccess)
def DeleteAllChaineTemporaires(token: dict=Depends(get_current_user), db: Session=Depends(get_db)) -> ResponseSuccess:
    userId = int(token["sub"])
    return deleteAllChaineTemporaires(userId=userId, db=db)