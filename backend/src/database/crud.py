from sqlalchemy.orm import Session

from src.auth import crypto

from . import models, schemas


def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = crypto.encrypt(user.password)
    db_user = models.User(
        name=user.name,
        registration=user.registration,
        email=user.email,
        hashed_password=hashed_password,
        is_confirmed=False,
        role=models.Role.user,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(email: str, db: Session) -> schemas.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_registration(registration: str, db: Session) -> schemas.User:
    return (
        db.query(models.User).filter(models.User.registration == registration).first()
    )
