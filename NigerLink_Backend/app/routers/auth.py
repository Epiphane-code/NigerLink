from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserLogin, TokenResponse
from app.core.security import password_vefify, create_access_token
from app.database.database import get_db
from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Public"]
)

@router.post("/login", response_model=TokenResponse)
def login(
    data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.scalar(
        select(User).where(
            or_(
                User.email == data.username,
                User.phone == data.username
            )
        )
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Identifiants incorrects"
        )

    password_correct = password_vefify(
        data.password,
        user.password
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Identifiants incorrects"
        )

    access_token = create_access_token({
        "sub": str(user.userId),
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }