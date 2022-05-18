from typing import Literal, Optional, Union
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


class AdminDoctorCreate(BaseModel):
    name: str
    email: EmailStr
    phone: constr(max_length=10, min_length=10)
    gender: Literal['male', 'female', 'other']
    dob: date
    about: str
    experience_year: int
    speciality: str
    registration_number: str


class DoctorOut(BaseModel):
    id: str
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
    slug: str
    total_patients: int = 0
    is_active: bool
    created_at: datetime
    updated_at: datetime
    is_banned: bool
    when_banned: Union[datetime, None]

    class Config:
        orm_mode = True


class DoctorOutUser(BaseModel):
    id: str
    name: str
    profile_image: str
    gender: str
    experience_year: int
    speciality: str
    slug: str
    is_verified: bool
    about: str

    class Config:
        orm_mode = True


class UpdateDoctorDetails(BaseModel):
    email: Optional[EmailStr]
    phone: Optional[constr(max_length=10, min_length=10)]
    about: Optional[str]
    profile_image: Optional[str]
