from sqlalchemy.orm import Session

from . import models, schemas

# gets

def get_prof(db: Session, id_prof_input: int):
    return db.query(models.Prof).filter(models.Prof.id_prof == id_prof_input).first()

def get_profs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prof).offset(skip).limit(limit).all()

def get_disciplina(db: Session, id_disc_input: int):
    return db.query(models.Disciplina).filter(models.Disciplina.id_disciplina == id_disc_input).first()

def get_disciplinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disciplina).offset(skip).limit(limit).all()

def get_discs_lecionadas(db: Session, id_prof_input: int):
    prof = db.query(models.Prof).filter(models.Prof.id_prof == id_prof_input).first()

    return prof.disciplinas_lecionadas

def get_profs_lecionando(db: Session, id_disc_input: int):
    disc = db.query(models.Disciplina).filter(models.Disciplina.id_disciplina == id_disc_input).first()

    return disc.professores_desta

# creates 

def criar_prof(db: Session, prof: schemas.ProfCreate):
    # instância de modelo do SQLAlchemy com os dados do objeto:
    db_prof = models.Prof(id_prof=prof.id, id_faculdade=prof.id_faculdade, 
                          nome=prof.nome, descricao=prof.descricao, nota=prof.nota)
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

