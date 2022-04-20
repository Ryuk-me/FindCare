from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateAdmin(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_super_admin: bool


class AdminOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_super_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
