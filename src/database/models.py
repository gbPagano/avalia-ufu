from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    
    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email})'
    

