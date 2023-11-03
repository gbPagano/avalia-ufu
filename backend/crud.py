from sqlalchemy.orm import Session

from . import models, schemas

# gets


def get_faculs(db: Session):
    return db.query(models.Faculdade).all()


def get_prof(db: Session, id_prof_input: int):
    return db.query(models.Prof).filter(models.Prof.id == id_prof_input).first()


def get_profs(sort: str | None, db: Session, skip: int = 0, limit: int = 100):
    if not sort:
        return db.query(models.Prof).offset(skip).limit(limit).all()

    if sort == "a-z":
        return (
            db.query(models.Prof)
            .order_by(models.Prof.nome)
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "z-a":
        return (
            db.query(models.Prof)
            .order_by(models.Prof.nome.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "nN":
        return (
            db.query(models.Prof)
            .order_by(models.Prof.nota)
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "Nn":
        return (
            db.query(models.Prof)
            .order_by(models.Prof.nota.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_profs_by_facul(id_facul: int, db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Prof)
        .filter(models.Prof.id_faculdade == id_facul)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_disciplina(db: Session, id_disc_input: int):
    return (
        db.query(models.Disciplina)
        .filter(models.Disciplina.id == id_disc_input)
        .first()
    )


def get_disciplinas(sort: str | None, db: Session, skip: int = 0, limit: int = 100):
    if not sort:
        return db.query(models.Disciplina).offset(skip).limit(limit).all()

    if sort == "a-z":
        return (
            db.query(models.Disciplina)
            .order_by(models.Disciplina.nome)
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "z-a":
        return (
            db.query(models.Disciplina)
            .order_by(models.Disciplina.nome.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "hard":
        return (
            db.query(models.Disciplina)
            .order_by(models.Disciplina.dificuldade.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif sort == "easy":
        return (
            db.query(models.Disciplina)
            .order_by(models.Disciplina.dificuldade)
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_discs_lecionadas(db: Session, id_prof_input: int):
    prof = db.query(models.Prof).filter(models.Prof.id == id_prof_input).first()

    return prof.disciplinas_lecionadas


def get_profs_lecionando(db: Session, id_disc_input: int):
    disc = (
        db.query(models.Disciplina)
        .filter(models.Disciplina.id == id_disc_input)
        .first()
    )

    return disc.professores_desta


def get_vinculos(db: Session):
    return db.query(models.Vinculo_Prof_Disc).all()


def get_reviews_disc(db: Session, id_disc: int):
    return db.query(models.Review).filter(models.Disciplina.id == id_disc).all()


def get_review(db: Session, id_review: int):
    return db.query(models.Review).filter(models.Review.id == id_review).first()


# creates


def criar_prof(db: Session, prof: schemas.Prof):
    # instância de modelo do SQLAlchemy com os dados do objeto:
    db_prof = models.Prof(
        id_prof=prof.id,
        id_faculdade=prof.id_faculdade,
        nome=prof.nome,
        descricao=prof.descricao,
        nota=prof.nota,
    )
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def criar_disc(db: Session, disc: schemas.Disciplina):
    db_disc = models.Disciplina(
        id_disciplina=disc.id, nome=disc.nome, id_faculdade=disc.id_faculdade
    )
    db.add(db_disc)
    db.commit()
    db.refresh(db_disc)
    return db_disc


def criar_vinculo_prof_disc(db: Session, vinculo: schemas.Vinculo_Prof_Disc):
    db_vinculo = models.Vinculo_Prof_Disc(
        id_vinculo=vinculo.id_vinculo,
        id_prof=vinculo.id_prof,
        id_disciplina=vinculo.id_disciplina,
    )
    db.add(db_vinculo)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo


def criar_facul(db: Session, facul: schemas.Faculdade):
    db_facul = models.Faculdade(id=facul.id, nome=facul.nome)
    db.add(db_facul)
    db.commit()
    db.refresh(db_facul)
    return db_facul


def criar_review(db: Session, review: schemas.CreateReview):
    try:
        db_review = models.Review(
            id_prof=review.id_prof,
            id_disc=review.id_disc,
            autor=review.autor,
            comentario=review.comentario,
            nota=review.nota,
            dif_disc=review.dif_disc,
            upvotes=review.upvotes,
        )
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review
    except Exception as err:
        print(err)


def vote(id_review: int, option: int, db: Session):
    try:
        db_review = db.query(models.Review).filter(models.Review.id == id_review).one()

        if option == 1:
            db_review.upvotes += 1
        else:
            db_review.upvotes -= 1

        db.commit()
        db.refresh(db_review)
        return db_review
    except Exception as err:
        print(err)
