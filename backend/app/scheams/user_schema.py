from datetime import datetime, date
from pydantic import BaseModel, EmailStr, constr
from typing import List, Literal, Optional, Union
from app.scheams import appointment_schema


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: constr(max_length=10, min_length=10)
    gender: Literal['male', 'female', 'other']
    dob: date
    password: str


class AdminUserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: constr(max_length=10, min_length=10)
    gender: Literal['male', 'female', 'other']
    dob: date


class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    profile_image: str
    gender: str
    phone:  str
    dob: date
    age: int
    is_active: bool
    is_banned: bool
    when_banned: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    appointments: List[appointment_schema.AppointmentOut]

    class Config:
        orm_mode = True


class UserOutAdminPanel(BaseModel):
    id: str
    name: str
    email: EmailStr
    gender: str
    phone:  str
    dob: date
    age: int
    is_active: bool
    is_banned: bool
    when_banned: Union[datetime, None]
    total_appointments: int = 0
    completed_appointments: int = 0
    cancelled_appointments_by_doctor: int = 0
    cancelled_appointments_by_user: int = 0
    pending_appointments: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UpdateUserDetails(BaseModel):
    name: Optional[str]
    email: Optional[str]
    profile_image: Optional[str]
    phone: Optional[constr(max_length=10, min_length=10)]
