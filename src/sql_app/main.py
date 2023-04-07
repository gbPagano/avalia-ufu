from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/profs/", response_model=schemas.Prof)
def criar_prof(prof: schemas.ProfCreate, db: Session = Depends(get_db)):
    return crud.criar_prof(db=db, prof=prof)

@app.get("/profs/", response_model=list[schemas.Prof])
def ler_profs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profs = crud.get_profs(db, skip=skip, limit=limit)
    return profs
