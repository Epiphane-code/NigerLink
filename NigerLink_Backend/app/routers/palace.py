from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_current_user
from app.database.database import get_db
from app.schemas.palace import PalaceCreate
from app.core.security import verify_access_token
from app.services_database.palace import palaceToBase, validerPalace, getPalaceTemp, getPalace, deleteAllPalaceTemp, deletePalace
from app.schemas.palace import ResponseGetPalace




router = APIRouter(
    prefix="/palace",
    tags=["Private"]
)

@router.post("/create", response_model=ResponseGetPalace)
def CreatePalace(palaceData : PalaceCreate, token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    idUser = int(token["sub"])
    return(
        palaceToBase(id= idUser, palace= palaceData, db= db)
    )
    
@router.post("/validerpalace", response_model=ResponseGetPalace)
def ValiderPalace(palaceId: int, token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return validerPalace(palaceId=int(palaceId), userId= int(token["sub"]), db=db)


@router.get("/getpalacestemporaires", response_model=List[ResponseGetPalace])
def GetPalaceTemp(token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    userId = token["sub"]
    return(getPalaceTemp(userId=int(userId),db=db))

routerPublic = APIRouter(
     prefix="/palace",
        tags=["Public"]
)
@router.delete("/deletePalace")
def DeletePalace(palaceId: int,token: dict = Depends(get_current_user),db: Session = Depends(get_db)):
    userId = int(token["sub"])
    return deletePalace(userId=userId, palaceId=palaceId, db=db)

@routerPublic.get("/getpalaces", response_model=ResponseGetPalace)
def GetPalace(db: Session = Depends(get_db)):
    return(getPalace(db=db))

routerPrivate2 = APIRouter(
    prefix="/palace",
    tags=["Private X2"]
)

@routerPrivate2.delete("/deleteAllPalaceTemp")
def DeleteAllPalaceTemp(token: dict = Depends(get_current_user),db: Session = Depends(get_db)):
    userId = int(token["sub"])
    return deleteAllPalaceTemp(userId=userId, db=db)





    