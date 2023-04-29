from fastapi import FastAPI, Depends

from src.auth.routes import app_auth
from src.database import models
from src.database.core import engine

from src.auth.token import get_current_confirmed_user

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(app_auth, prefix="")


@app.get("/{prof}")
def test(
    prof: str,
    _ = Depends(get_current_confirmed_user)
):
    return {"professor": prof}

@app.get("/")
def index():
    return {"hello": "world"}
