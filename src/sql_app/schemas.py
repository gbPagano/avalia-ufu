from pydantic import BaseModel

# contém somente models do pydantic

class DisciplinaBase(BaseModel):
    nome: str

class ProfBase(BaseModel):
    nome: str
    descricao: str
    nota: float

class DisciplinaCreate(DisciplinaBase):
    id: int
    id_faculdade: int

class ProfCreate(ProfBase):
    id: int
    id_faculdade: int

class Disciplina(DisciplinaBase):
    professores_desta: list["Prof"] = []

    class Config:
        orm_mode = True

class Prof(ProfBase):
    disciplinas_lecionadas: list[Disciplina] = []
    
    class Config:
        orm_mode = True

Disciplina.update_forward_refs()







    