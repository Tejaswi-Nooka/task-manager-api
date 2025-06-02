from pydantic import BaseModel
from typing import Optional, List


# ------------- User Schemas -------------

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str  # Only used when registering

class User(UserBase):
    id: int

    class Config:
        orm_mode = True  # Allows ORM objects (from SQLAlchemy) to work with Pydantic


# ------------- Task Schemas -------------

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass  # Same fields as TaskBase

class Task(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True


# ------------- JWT Token Schemas -------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
