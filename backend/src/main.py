from fastapi import FastAPI

from src.database.core import engine
from src.database import models
from src.auth.routes import app_auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(app_auth)

@app.get("/")
def index():
    return {"hello": "world"}
