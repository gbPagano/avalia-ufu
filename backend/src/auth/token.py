from datetime import datetime, timedelta
from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Request

from jose import jwt, JWTError


from src.database import crud, core, schemas

SECRET_KEY = "W7S6ECEWiOdu6OGGV_uUtS_l-pIjg4dwVPjMGOePeMw="
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 hours




InvalidCredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
)

ExpiredTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token has expired",
)

UnconfirmedAccountException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Unconfirmed account",
)


def create_access_token(data: dict, minutes: int = 15):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def get_current_token(request: Request):
    
    token = request.cookies.get("access-token")
    if not token:
        raise InvalidCredentialsException

    return token


def get_current_user(token: Annotated[str, Depends(get_current_token)], db: Session = Depends(core.get_db)):
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


def get_current_confirmed_user(
    user: schemas.User = Depends(get_current_user) 
):
    if not user.is_confirmed:
        raise UnconfirmedAccountException
        
    return user
