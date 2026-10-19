from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.database.database import get_db
from app.schemas.diffusion import CreateDiffusionModel, ResponseGetDiffusion
from app.schemas.success import ResponseSuccess
from app.services_database.diffusion import createDiffusion, deleteDiffusion, getDiffusions

router = APIRouter(
    prefix="/diffusion",
    tags=["Private"]
)

@router.post("/createDiffusion", response_model=ResponseGetDiffusion)
def CreateDiffusion(diff: CreateDiffusionModel, token: dict=Depends(get_current_user),db: Session=Depends(get_db) ):
    userId = int(token["sub"])
    return createDiffusion(diffusion=diff, userId=userId, db=db)

@router.delete("/deleteDiffusion", response_model=ResponseSuccess)
def DeleteDiffusion(diffusionId: int, chaineId: int, token: dict=Depends(get_current_user), db:Session=Depends(get_db) ):
    userId = int(token["sub"])
    return deleteDiffusion(diffusionId=diffusionId, chaineId=chaineId, userId=userId, db=db)

routerPublic = APIRouter(
    prefix="/diffusion",
    tags=["Public"]
)

@routerPublic.get("/getAllDiffusions", response_model=List[ResponseGetDiffusion])
def GetDiffusions(db:Session=Depends(get_db)):
    return getDiffusions(db=db)