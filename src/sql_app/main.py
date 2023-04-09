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
def criar_prof(prof: schemas.Prof, db: Session = Depends(get_db)):
    return crud.criar_prof(db=db, prof=prof)

@app.get("/profs/", response_model=list[schemas.Prof])
def ler_profs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profs = crud.get_profs(db, skip=skip, limit=limit)
    return profs

@app.post("/discs/", response_model=schemas.Disciplina)
def criar_disc(disc: schemas.Disciplina, db: Session = Depends(get_db)):
    return crud.criar_disc(db=db, disc=disc)

@app.get("/discs/", response_model=list[schemas.Disciplina])
def ler_discs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    discs = crud.get_disciplinas(db=db, skip=skip, limit=limit)
    return discs

@app.post("/vinculos/", response_model=schemas.VinculoProfDisc)
def registrar_vinculo_prof_disc(vinculo: schemas.VinculoProfDisc, db: Session = Depends(get_db)):
    return crud.criar_vinculo_prof_disc(db=db, vinculo=vinculo)

@app.get("/vinculos/", response_model=list[schemas.VinculoProfDisc])
def get_vinculos(db: Session = Depends(get_db)):
    return crud.get_vinculos(db)

