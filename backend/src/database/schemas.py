import re

from pydantic import BaseModel, validator

from .models import Role


class UserBase(BaseModel):
    name: str
    email: str
    registration: str

    @validator("email")
    def validate_email(cls, email):
        pattern = r"\b[A-Za-z0-9._%+-]+@ufu.br\b"
        if not re.match(pattern, email):
            raise ValueError("it's not an email from ufu")
        return email


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    is_confirmed: bool
    role: Role

    class Config:
        orm_mode = True
