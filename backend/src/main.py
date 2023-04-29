from fastapi import Depends, FastAPI

from src.auth.routes import app_auth
from src.auth.token import manager
from src.database import models
from src.database.core import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(app_auth, prefix="")


@app.get("/{prof}")
def test(prof: str, _=Depends(manager.current_confirmed_user)):
    return {"professor": prof}


@app.get("/")
def index():
    return {"hello": "world"}
