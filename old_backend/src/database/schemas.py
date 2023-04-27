from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    registration: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    is_confirmed: bool
    role: str

    class Config:
        orm_mode = True
