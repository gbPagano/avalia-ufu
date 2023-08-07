from __future__ import annotations

from pydantic import BaseModel

# contém somente models do pydantic

class Faculdade(BaseModel):
    id_faculdade: int
    nome: str

    class Config:
        orm_mode = True

class Disciplina(BaseModel):
    id_disciplina: int
    id_faculdade: int

    nome: str

    professores_desta: list[Prof] = []

    class Config:
        orm_mode = True

class Prof(BaseModel):
    id_prof: int
    id_faculdade: int

    nome: str
    descricao: str
    nota: float

    disciplinas_lecionadas: list[Disciplina] = []
    
    class Config:
        orm_mode = True

class VinculoProfDisc(BaseModel):
    id_vinculo: int
    id_prof: int
    id_disciplina: int

    class Config:
        orm_mode = True
    
# necessário pois a classe Disciplina usa uma entidade Prof que é criada posteriormente
Disciplina.model_rebuild()









    