from __future__ import annotations

from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, Mapped

from .database import Base

# contém somente models do sqlalchemy

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
                                          back_populates="professores_desta",
                                          lazy="joined")

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id_disciplina = Column(Integer, primary_key=True, index=True)
    id_faculdade = Column(Integer, ForeignKey("faculdades.id_faculdade"), nullable=False, index=True)

    nome = Column(String, nullable=False, index=True)

    #disc1.professores_desta
    professores_desta = relationship("Prof",
                                    secondary="vinculos_profs_discs",
                                    back_populates="disciplinas_lecionadas",
                                    lazy="joined") 

class Vinculos_Profs_Discs(Base):
    __tablename__ = "vinculos_profs_discs"

    id_vinculo = Column(Integer, primary_key=True, index=True)
    id_prof = Column(Integer, ForeignKey("profs.id_prof"), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id_disciplina"), primary_key=True)

class Review(Base):
    __tablename__ = "reviews"

    id_review = Column(Integer, primary_key=True, index=True)
    id_prof = Column(Integer, ForeignKey("profs.id_prof"), nullable=False, index=True)    
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id_disciplina"), nullable=False, index=True)

    nome = Column(String, nullable=False, index=True)
    comentario = Column(String, nullable=False, index=True)
    nota = Column(Float, nullable=False, index=True)
    upvotes = Column(Integer, nullable=False, index=True)

class Faculdade(Base):
    __tablename__ = "faculdades"

    id_faculdade = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)