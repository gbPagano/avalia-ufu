from pydantic import BaseModel

# contém somente models do pydantic

class Disciplina(BaseModel):
    id_disciplina: int
    id_faculdade: int

    nome: str

    professores_desta: list["Prof"] = []

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

# necessário pois a classe Disciplina usa uma entidade Prof que é criada posteriormente
Disciplina.update_forward_refs()

class VinculoProfDisc(BaseModel):
    id_vinculo: int
    id_prof: int
    id_disciplina: int

    class Config:
        orm_mode = True
    








    