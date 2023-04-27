from datetime import timedelta

from fastapi import APIRouter, HTTPException, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

from src.database import schemas, crud
from src.database.core import get_db
from .crypto import decrypt
from .token import manager, send_confirmation_email

app_auth = APIRouter(
    prefix="",
    tags=["authentication"],
)


@app_auth.post("/register")
def register(
    response: Response,
    user: schemas.UserCreate,
):
    db_user = crud.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(user=user)
    
    access_token = manager.create_access_token(
        data={'sub': new_user.email}, expires=timedelta(minutes=15)
    )
    
    print("send email:", access_token)  
    send_confirmation_email(access_token, "guilhermebpagano@gmail.com")
    
    manager.set_cookie(response, access_token)
    response.status_code = 200
    return response 


@app_auth.get('/logout')
def logout(response: Response, _=Depends(manager)):
    manager.set_cookie(response, "")
    response.status_code = 200
    return response




@app_auth.post('/login')
def login(
    response: Response,
    data: OAuth2PasswordRequestForm = Depends(),
):
    email = data.username
    password = data.password

    user = crud.get_user_by_email(email)
    if not user or not decrypt(user.hashed_password, password):
        raise InvalidCredentialsException
 
    access_token = manager.create_access_token(
        data={'sub': email}, expires=timedelta(hours=12)
    )
    manager.set_cookie(response, access_token)
    response.status_code = 200
    return response 




@app_auth.get('/user/confirm-account/{token}')
def confirm_account(response: Response, token: str, validate_email: str = "", db: Session=Depends(get_db)):
    import jwt
    try:
        email = jwt.decode(token, "super-secret-key", algorithms=["HS256"])["sub"]
    except Exception as err:
        return {"error": err}
    
    user = crud.get_user_by_email(email, db=db)
    if not user:
        return {"error": "credentials invalid"}
    elif user.is_confirmed:
        return {"error": "your account has already been activated"}
    elif user.email == validate_email:
        user.is_confirmed = True
    
    db.commit()
    
    manager.set_cookie(response, token)
    response.status_code = 200
    return response






