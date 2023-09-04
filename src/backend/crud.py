from sqlalchemy.orm import Session

import models, schemas

# gets

def get_prof(db: Session, id_prof_input: int):
    return db.query(models.Prof).filter(models.Prof.id_prof == id_prof_input).first()

def get_profs(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Prof).offset(skip).limit(limit).all()

    return query

def get_disciplina(db: Session, id_disc_input: int):
    return db.query(models.Disciplina).filter(models.Disciplina.id_disciplina == id_disc_input).first()

def get_disciplinas(db: Session, skip: int = 0, limit: int = 100):
    discs = db.query(models.Disciplina).offset(skip).limit(limit).all()

    return discs

def get_discs_lecionadas(db: Session, id_prof_input: int):
    prof = db.query(models.Prof).filter(models.Prof.id_prof == id_prof_input).first()

    return prof.disciplinas_lecionadas

def get_profs_lecionando(db: Session, id_disc_input: int):
    disc = db.query(models.Disciplina).filter(models.Disciplina.id_disciplina == id_disc_input).first()

    return disc.professores_desta

def get_vinculos(db: Session):
    return db.query(models.Vinculo_Prof_Disc).all();

def get_reviews_disc(db: Session, id_disc: int):
    return db.query(models.Review).filter(models.Disciplina.id_disciplina == id_disc).all()

# creates 

def criar_prof(db: Session, prof: schemas.Prof):
    # instância de modelo do SQLAlchemy com os dados do objeto:
    db_prof = models.Prof(id_prof=prof.id_prof, id_faculdade=prof.id_faculdade, 
                          nome=prof.nome, descricao=prof.descricao, nota=prof.nota)
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof

def criar_disc(db: Session, disc: schemas.Disciplina):
    db_disc = models.Disciplina(id_disciplina=disc.id_disciplina, nome=disc.nome, id_faculdade=disc.id_faculdade)
    db.add(db_disc)
    db.commit()
    db.refresh(db_disc)
    return db_disc

def criar_vinculo_prof_disc(db: Session, vinculo: schemas.Vinculo_Prof_Disc):
    db_vinculo = models.Vinculo_Prof_Disc(id_vinculo=vinculo.id_vinculo, 
                                             id_prof=vinculo.id_prof, 
                                             id_disciplina=vinculo.id_disciplina)
    db.add(db_vinculo)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo

def criar_facul(db: Session, facul: schemas.Faculdade):
    db_facul = models.Faculdade(id_faculdade=facul.id_faculdade, nome=facul.nome)
    db.add(db_facul)
    db.commit()
    db.refresh(db_facul)
    return db_facul