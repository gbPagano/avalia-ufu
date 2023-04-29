from datetime import datetime, timedelta

from fastapi import Depends, Request
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.database import core, crud

from .exceptions import InvalidCredentialsException, UnconfirmedAccountException

SECRET_KEY = "W7S6ECEWiOdu6OGGV_uUtS_l-pIjg4dwVPjMGOePeMw="
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 hours


class LoginManager:
    def __init__(self, secret_key: str, default_minutes_token_expire: int):
        self.secret_key = secret_key
        self.default_minutes_token_expire = default_minutes_token_expire
        self.jwt_algorithm = "HS256"
        self.cookie_name = "access-token"

    def create_access_token(self, data: dict, minutes: int = 0):
        if not minutes:
            minutes = self.default_minutes_token_expire
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, self.secret_key, algorithm=self.jwt_algorithm
        )
        return encoded_jwt

    def current_token(self, request: Request):
        token = request.cookies.get(self.cookie_name)
        if not token:
            raise InvalidCredentialsException

        return token

    def current_user(self, request: Request, db: Session = Depends(core.get_db)):
        token = self.current_token(request)
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=self.jwt_algorithm)
            email = payload.get("sub")
            if email is None:
                raise InvalidCredentialsException
        except JWTError:
            raise InvalidCredentialsException

        user = crud.get_user_by_email(email, db)
        if not user:
            raise InvalidCredentialsException

        return user

    def current_confirmed_user(
        self, request: Request, db: Session = Depends(core.get_db)
    ):
        user = self.current_user(request, db)
        if not user.is_confirmed:
            raise UnconfirmedAccountException

        return user


manager = LoginManager(
    secret_key=SECRET_KEY, default_minutes_token_expire=60 * 8  # 8 hours
)
