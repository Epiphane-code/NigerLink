from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    print("TOKEN REÇU :", token)

    payload = verify_access_token(token)

    print("PAYLOAD :", payload)

    return payload