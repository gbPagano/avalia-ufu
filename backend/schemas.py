from __future__ import annotations

import re

from models import Role

from pydantic import BaseModel, validator

# contém somente models do pydantic

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


class Faculdade(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True


class Disciplina(BaseModel):
    id: int
    id_faculdade: int

    nome: str
    dificuldade: float

    professores_desta: list[Prof] = []
    reviews_desta: list[Review] = []

    class Config:
        orm_mode = True


class Prof(BaseModel):
    id: int
    id_faculdade: int

    nome: str
    descricao: str
    nota: float

    disciplinas_lecionadas: list[Disciplina] = []

    class Config:
        orm_mode = True


class Vinculo_Prof_Disc(BaseModel):
    id: int
    id_prof: int
    id_disc: int

    class Config:
        orm_mode = True


class Review(BaseModel):
    id: int
    id_prof: int
    id_disc: int

    autor: str
    comentario: str
    nota: float
    dif_disc: float
    upvotes: int

    class Config:
        orm_mode = True


class CreateReview(BaseModel):
    id_prof: int
    id_disc: int
    autor: str
    comentario: str
    nota: float
    dif_disc: float
    upvotes: int


# necessário pois a classe Disciplina usa a entidade Prof que é criada posteriormente
Disciplina.model_rebuild()
