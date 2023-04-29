from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated
from src.database import core, crud, schemas
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .token import InvalidCredentialsException, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user, ExpiredTokenException
from datetime import datetime, timedelta
from .crypto import decrypt, simetric_encrypt, simetric_decrypt
from .email_sender import send_confirmation_email


class Token(BaseModel):
    access_token: str
    token_type: str

app_auth = APIRouter(
    prefix="",
    tags=["authentication"],

    )
@app_auth.post('/login')
def login(
    data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(core.get_db),
):
    email = data.username
    password = data.password

    user = crud.get_user_by_email(email, db)
    if not user or not decrypt(user.hashed_password, password):
        raise InvalidCredentialsException
 
    return user

@app_auth.post("/register")
def register(
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

    return new_user

@app_auth.post("/token", response_model=Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(core.get_db),
):
    email = form_data.username
    password = form_data.password
    user = crud.get_user_by_email(email, db)
    if not user or not decrypt(user.hashed_password, password):
        raise InvalidCredentialsException

    access_token = create_access_token(
        data={"sub": user.email}, minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {"access_token": access_token, "token_type": "bearer"}


from .token import get_current_user, InvalidCredentialsException, SECRET_KEY
from src.database.schemas import User
from jose import jwt, JWTError, ExpiredSignatureError

@app_auth.get('/confirm-account/{token}')
def confirm_account(token: str, tgt: str, db: Session = Depends(core.get_db)):
    email_target = simetric_decrypt(tgt)
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
        return payload
    #     raise HTTPException(status_code=409, detail="Account has already been activated")

    user.is_confirmed = True
    db.commit()
    
    user = crud.get_user_by_email(email, db)
    return user
    




@app_auth.get("/me", response_model=User)
def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    print(current_user)
    print(current_user.role)
    print(type(current_user.role))
    return current_user
