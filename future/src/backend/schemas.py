from __future__ import annotations

from pydantic import BaseModel

# contém somente models do pydantic


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
