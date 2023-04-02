from src.auth.crypto import encrypt
from src.auth.token import manager
from . import models, schemas
from .core import DBContext


@manager.user_loader()
def get_user_by_email(email: str) -> schemas.User:
    with DBContext() as db:
        return db.query(models.User).filter(models.User.email == email).first()


def create_user(user: schemas.UserCreate):
    with DBContext() as db:
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

