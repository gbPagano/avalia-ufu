from fastapi import Depends, FastAPI

from src.database.core import engine
from src.database import models
from src.auth.token import manager, NotAuthenticatedException, auth_exception_handler
from src.auth.routes import app_auth


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

manager.useRequest(app)

app.add_exception_handler(NotAuthenticatedException, auth_exception_handler)


app.include_router(app_auth)



@app.get("/")
def root(user=Depends(manager)):
    return user


@app.get("/prof/{name}")
def profile_prof(name: str, user=Depends(manager)):
    if not user.is_confirmed:
        return {"error": "confirme sua conta"}
    return {"professor": name}


