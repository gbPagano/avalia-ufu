from datetime import datetime, timedelta
from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

from src.database import crud, core

SECRET_KEY = "dbec0c9fdcd9cffae832de157a223e79213b47620045a40ad3591cfa77c08857"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

InvalidCredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
    headers={"WWW-Authenticate": "Bearer"}
)


def create_access_token(data: dict, minutes: int = 15):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(core.get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload.get("sub")
        if email is None:
            raise InvalidCredentialsException
    except JWTError:
        raise InvalidCredentialsException

    user = crud.get_user_by_email(email, db)
    if not user:
        raise InvalidCredentialsException

    return user




