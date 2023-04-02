from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from src.database.core import engine
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
def profile_prof(name: str, _=Depends(manager)):
    return {"professor": name}


@app.post("/register")
def register(
    user: schemas.UserCreate,
):
    db_user = crud.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user)


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

