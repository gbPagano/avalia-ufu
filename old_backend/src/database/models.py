from sqlalchemy import Boolean, Column, Integer, String

from .core import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    registration = Column(String, unique=True, index=True) 
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_confirmed = Column(Boolean)
    role = Column(String)
    
