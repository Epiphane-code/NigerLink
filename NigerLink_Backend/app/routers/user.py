from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_current_user
from app.database.database import get_db
from app.schemas.user import UserCreate
from app.services_database.user import userToBase, getUsers, getMe, restorePassword
from app.schemas.user import UserInfo, ResponseRestorePassword
from app.schemas.success import ResponseSuccess

router = APIRouter(
    prefix="/auth",
    tags=["Private"]
)
@router.get("/getMe", response_model=UserInfo)
def GetMe(
    token : dict=Depends(get_current_user),
    db: Session= Depends(get_db)
):
    userId = int(token["sub"])
    return getMe(userId=userId, db=db)
    
@router.get("/getUsers", response_model=List[UserInfo])
def GetUsers(token: dict = Depends(get_current_user), db: Session = Depends(get_db)) -> List[UserInfo]:
    userId = int(token["sub"])
    return getUsers(userId=userId, db=db)

@router.put("/restorePassword", response_model=ResponseRestorePassword)
def RestorePassword(userId: int,token: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    adminId = int(token["sub"])
    return restorePassword(userId= userId, adminId= adminId, db=db)



routerPublic = APIRouter(
    prefix="/auth",
    tags=["Public"]
)
@routerPublic.post("/register", response_model=ResponseSuccess)
def CreateUser(
    userInfo: UserCreate,
    db: Session = Depends(get_db)
):
    return userToBase(
        userInfo=userInfo,
        db=db
    )
    