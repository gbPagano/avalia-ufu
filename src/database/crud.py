from sqlalchemy.orm import Session
 
from src.auth import encrypt
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = encrypt(user.password)
    db_user = models.User(
        name=user.name,
        registration=user.registration,
        email=user.email, 
        hashed_password=hashed_password,
        is_confirmed=False,
        role="user",
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

