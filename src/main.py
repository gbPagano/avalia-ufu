from datetime import timedelta
from email.message import EmailMessage, Message

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from src.database.core import engine, get_db
from src.database import schemas, crud, models
from src.auth.crypto import decrypt
from src.auth.token import manager, NotAuthenticatedException

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

manager.useRequest(app)

@app.exception_handler(NotAuthenticatedException)
def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    """
    Redirect the user to the login page if not logged in
    """
    return RedirectResponse(url='/login')


@app.get("/")
def root(user=Depends(manager)):
    return user


@app.get("/prof/{name}")
def profile_prof(name: str, user=Depends(manager)):
    if not user.is_confirmed:
        return {"error": "confirme sua conta"}
    return {"professor": name}


@app.post("/register")
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


@app.post('/login')
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


@app.get('/logout')
def logout(response: Response, _=Depends(manager)):
    manager.set_cookie(response, "")
    response.status_code = 200
    return response
 
@app.get('/user/confirm-account/{token}')
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





def send_confirmation_email(token: str, email_target: str):

    msg = EmailMessage()

    email_sender = "guilhermebpagano2@gmail.com"

    msg['Subject'] = f'Confirmação de cadastro - App Wiki UFU'
    msg['From'] = email_sender
    msg['To'] = email_target
    msg.set_content(
        f"""\
        Click no link abaixo para validar a sua conta:
        http://localhost:8080/user/confirm-account/{token}?validate_email={email_target}
        """,
    )

    import smtplib, ssl

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, "tflpjfmwqlbpenkv")
        server.sendmail(email_sender, email_target, msg.as_string())
