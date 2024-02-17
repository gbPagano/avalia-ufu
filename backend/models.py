from __future__ import annotations

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship 

from database import Base

import enum

# contém somente models do sqlalchemy

class Role(enum.Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"
    prof = "prof"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    registration = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_confirmed = Column(Boolean)
    role = Column(Enum(Role))


class Prof(Base):
    __tablename__ = "profs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_faculdade = Column(Integer, ForeignKey("faculdades.id"), nullable=False)

    nome = Column(String, index=True, nullable=False)
    descricao = Column(String, index=True)
    nota = Column(Float, index=True)

    # prof1.disciplinas_lecionadas
    disciplinas_lecionadas = relationship(
        "Disciplina",
        secondary="vinculos_profs_discs",
        back_populates="professores_desta",
        lazy="joined",
    )

    faculdade = relationship("Faculdade", lazy="joined")


class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_faculdade = Column(
        Integer, ForeignKey("faculdades.id"), nullable=False, index=True
    )

    nome = Column(String, nullable=False, index=True)
    dificuldade = Column(Float, nullable=False, index=True)

    # disc1.professores_desta
    professores_desta = relationship(
        "Prof",
        secondary="vinculos_profs_discs",
        back_populates="disciplinas_lecionadas",
        lazy="joined",
    )

    reviews_desta = relationship("Review", lazy="joined")
    faculdade = relationship("Faculdade", lazy="joined")


class Vinculo_Prof_Disc(Base):
    __tablename__ = "vinculos_profs_discs"

    id_vinculo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_prof = Column(Integer, ForeignKey("profs.id"))
    id_disc = Column(Integer, ForeignKey("disciplinas.id"))


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_prof = Column(Integer, ForeignKey("profs.id"), nullable=False, index=True)
    id_disc = Column(Integer, ForeignKey("disciplinas.id"), nullable=False, index=True)

    autor = Column(String, nullable=False, index=True)
    comentario = Column(String, nullable=False, index=True)
    nota = Column(Float, nullable=False, index=True)
    dif_disc = Column(Float, nullable=False, index=True)
    upvotes = Column(Integer, nullable=False, index=True)

    professor = relationship("Prof", lazy="joined")
    # kjodasod


class Faculdade(Base):
    __tablename__ = "faculdades"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False, index=True)
