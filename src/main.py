from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.database.core import get_db, engine
from src.database import schemas, crud, models



app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/prof/{name}")
def profile_prof(name: str):
    return {"professor": name}


@app.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



