from typing import Literal
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime, date


class DoctorCreate(BaseModel):
    name: str
    email: EmailStr
    phone: constr(max_length=10, min_length=10)
    gender: Literal['male', 'female', 'other']
    dob: date
    password: str
    about: str
    experience_year: int
    speciality: str
    registration_number: str


class DoctorOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: constr(max_length=10, min_length=10)
    profile_image: str
    gender: str
    dob: date
    age: int
    about: str
    experience_year: int
    speciality: str
    registration_number: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
