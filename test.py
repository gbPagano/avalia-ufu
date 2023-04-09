from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Prof(Base):
    __tablename__ = "profs"

    id_prof = Column(Integer, primary_key=True, index=True)
    id_faculdade = Column(Integer, ForeignKey("faculdades.id_faculdade"), nullable=False)

    nome = Column(String, index=True, nullable=False)
    descricao = Column(String, index=True)
    nota = Column(Float, index=True)

    # prof1.disciplinas_lecionadas
    disciplinas_lecionadas = relationship("Disciplina", 
                                          secondary="vinculos_profs_discs",
                                          back_populates="professores_desta")
    
    def __repr__(self):
        discs_lecionadas_nomes = [d.nome for d in self.disciplinas_lecionadas]

        return f'Prof(nome={self.nome}, id_prof={self.id_prof}, discs_lecionadas={discs_lecionadas_nomes})'

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id_disciplina = Column(Integer, primary_key=True, index=True)
    id_faculdade = Column(Integer, ForeignKey("faculdades.id_faculdade"), nullable=False, index=True)

    nome = Column(String, nullable=False, index=True)

    #disc1.professores_desta
    professores_desta = relationship("Prof",
                                    secondary="vinculos_profs_discs",
                                    back_populates="disciplinas_lecionadas") 
    
    def __repr__(self):
        profs_desta = [p.nome for p in self.professores_desta]

        return f'Disciplina(nome={self.nome}, profs_desta={profs_desta})'

class Vinculos_Profs_Discs(Base):
    __tablename__ = "vinculos_profs_discs"

    id_vinculo = Column(Integer, primary_key=True, index=True)
    id_prof = Column(Integer, ForeignKey("profs.id_prof"), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id_disciplina"), primary_key=True)

    def __repr__(self):
        return f'Vinculo(id_prof={self.id_prof}, id_disc={self.id_disciplina})'



class Faculdade(Base):
    __tablename__ = "faculdades"

    id_faculdade = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)


Base.metadata.create_all(engine)

facul = Faculdade(id_faculdade=1, nome="famat")
disc1 = Disciplina(id_disciplina=1, id_faculdade=1, nome="calculo1")
disc2 = Disciplina(id_disciplina=2, id_faculdade=1, nome="metodos")
disc3 = Disciplina(id_disciplina=3, id_faculdade=1, nome="algebra")
prof1 = Prof(id_prof=1, id_faculdade=1, nome="aaa", descricao="aaasda", nota=10)
prof2 = Prof(id_prof=2, id_faculdade=1, nome="bbb", descricao="asda", nota=10)
prof3 = Prof(id_prof=3, id_faculdade=1, nome="ccc", descricao="axzc", nota=10)
vinculo1 = Vinculos_Profs_Discs(id_vinculo=1, id_prof=1, id_disciplina=1)
vinculo2 = Vinculos_Profs_Discs(id_vinculo=2, id_prof=1, id_disciplina=2)
vinculo3 = Vinculos_Profs_Discs(id_vinculo=3, id_prof=1, id_disciplina=3)
vinculo4 = Vinculos_Profs_Discs(id_vinculo=4, id_prof=2, id_disciplina=1)
vinculo5 = Vinculos_Profs_Discs(id_vinculo=5, id_prof=3, id_disciplina=1)


session.add_all([facul, prof1, prof2, prof3, disc1, disc2, disc3, vinculo1, vinculo2, vinculo3, vinculo4, vinculo5])

session.commit()

from pprint import pprint

pprint(session.query(Prof).first())
pprint(session.query(Disciplina).all())