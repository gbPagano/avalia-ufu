from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/faculs/", response_model=schemas.Faculdade)
def criar_facul(facul: schemas.Faculdade, db: Session = Depends(get_db)):
    return crud.criar_facul(db=db, facul=facul)


@app.post("/profs/", response_model=schemas.Prof)
def criar_prof(prof: schemas.Prof, db: Session = Depends(get_db)):
    return crud.criar_prof(db=db, prof=prof)


@app.get("/faculs/")
def get_faculs(db: Session = Depends(get_db)):
    return crud.get_faculs(db=db)


@app.get("/profs/")
def ler_profs(
    sort: str | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    profs = crud.get_profs(sort=sort, db=db, skip=skip, limit=limit)
    return profs


@app.get("/profs/{id_facul}")
def get_profs_by_facul(
    id_facul: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_profs_by_facul(id_facul=id_facul, skip=skip, limit=limit, db=db)


@app.post("/discs/", response_model=schemas.Disciplina)
def criar_disc(disc: schemas.Disciplina, db: Session = Depends(get_db)):
    return crud.criar_disc(db=db, disc=disc)


@app.get("/discs/")
def ler_discs(
    sort: str | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    discs = crud.get_disciplinas(sort=sort, db=db, skip=skip, limit=limit)
    return discs


@app.get("/discs/{disc_id}")
def ler_disc(disc_id, db: Session = Depends(get_db)):
    return crud.get_disciplina(db=db, id_disc_input=disc_id)


@app.post("/vinculos/", response_model=schemas.Vinculo_Prof_Disc)
def registrar_vinculo_prof_disc(
    vinculo: schemas.Vinculo_Prof_Disc, db: Session = Depends(get_db)
):
    return crud.criar_vinculo_prof_disc(db=db, vinculo=vinculo)


@app.get("/vinculos/", response_model=list[schemas.Vinculo_Prof_Disc])
def get_vinculos(db: Session = Depends(get_db)):
    return crud.get_vinculos(db)


@app.get("/discs/{id_disc}/reviews")
def ler_reviews_disc(id_disc: int, db: Session = Depends(get_db)):
    return crud.get_reviews_disc(db=db, id_disc=id_disc)


@app.get("/reviews/{id_review}")
def ler_review(id_review: int, db: Session = Depends(get_db)):
    return crud.get_review(db=db, id_review=id_review)


@app.post("/reviews/{id_review}/vote")
def vote(id_review: int, option: int, db: Session = Depends(get_db)):
    try:
        return crud.vote(id_review=id_review, option=option, db=db)
    except Exception as err:
        print(err)


@app.post("/reviews/")
def criar_review(review: schemas.CreateReview, db: Session = Depends(get_db)):
    try:
        return crud.criar_review(db=db, review=review)
    except Exception as err:
        print(err)
