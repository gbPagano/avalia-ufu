from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from jose import ExpiredSignatureError, JWTError, jwt
from sqlalchemy.orm import Session

from src.database import core, crud, schemas
from src.database.schemas import User

from .crypto import decrypt, symmetric_decrypt
from .email_sender import send_confirmation_email
from .exceptions import ExpiredTokenException, InvalidCredentialsException
from .token import SECRET_KEY, manager


app_auth = APIRouter(
    prefix="",
    tags=["authentication"],
)


@app_auth.post("/register")
def register(
    response: Response,
    user: schemas.UserCreate,
    db: Session = Depends(core.get_db),
):
    userdb_email = crud.get_user_by_email(email=user.email, db=db)
    userdb_registration = crud.get_user_by_registration(
        registration=user.registration, db=db
    )
    if userdb_email or userdb_registration:
        raise HTTPException(status_code=400, detail="User already registered")

    new_user = crud.create_user(user=user, db=db)

    send_confirmation_email(user.email)

    access_token = manager.create_access_token(data={"sub": user.email})
    response.set_cookie(key="access-token", value=access_token, httponly=True)

    return new_user


@app_auth.post("/login")
def login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(core.get_db),
):
    email = form_data.username
    password = form_data.password
    user = crud.get_user_by_email(email, db)
    if not user or not decrypt(user.hashed_password, password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"sub": user.email})
    response.set_cookie(key="access-token", value=access_token, httponly=True)

    return user


@app_auth.post("/logout")
def logout(
    response: Response,
):
    response.set_cookie(key="access-token", value="", httponly=True)
    response.status_code = 200
    return response


@app_auth.get("/confirm-account/{token}")
def confirm_account(token: str, tgt: str, db: Session = Depends(core.get_db)):
    email_target = symmetric_decrypt(tgt)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload.get("sub")
        if email is None or email != email_target:
            raise InvalidCredentialsException
    except ExpiredSignatureError:
        send_confirmation_email(email_target)
        raise ExpiredTokenException
    except JWTError:
        raise InvalidCredentialsException

    user = crud.get_user_by_email(email, db)
    if not user:
        raise InvalidCredentialsException

    if user.is_confirmed:
        raise HTTPException(
            status_code=409, detail="Account has already been activated"
        )

    user.is_confirmed = True
    db.commit()

    user = crud.get_user_by_email(email, db)
    return user


@app_auth.get("/me", response_model=User)
def read_users_me(current_user: Annotated[User, Depends(manager.current_user)]):
    return current_user
