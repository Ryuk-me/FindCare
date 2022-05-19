from typing import List, Optional, Union
from pydantic import BaseModel, constr, EmailStr
from datetime import time, date, datetime
from app.scheams import doctor_schema


class _ClinicAddress(BaseModel):
    pincode: constr(max_length=6, min_length=6)
    address: str
    city: str
    state: str


class AppointmentOutUser(BaseModel):
    id: str
    schedule: datetime
    fees_paid: bool
    is_completed: bool
    is_cancelled: Union[str, None]
    when_cancelled: Union[datetime, None]
    created_at: datetime

    class Config:
        orm_mode = True


class UserOutDoctorPanel(BaseModel):
    id: str
    name: str
    email: EmailStr
    gender: str
    phone:  str
    profile_image: str
    age: int
    appointments: List[AppointmentOutUser]

    class Config:
        orm_mode = True


class ClinicCreate(BaseModel):
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    is_open: Optional[bool] = False
    address:  _ClinicAddress


class ClinicOut(BaseModel):
    id: str
    doctor_id: str
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: int
    is_open: bool
    address: _ClinicAddress
    doctor: doctor_schema.DoctorOut
    patients: Union[List[UserOutDoctorPanel], None]
    total_patients: int = 0
    today_appointments: int = 0
    total_appointments: int = 0
    completed_appointments: int = 0
    cancelled_appointments_by_doctor: int = 0
    cancelled_appointments_by_user: int = 0
    pending_appointments: int = 0

    class Config:
        orm_mode = True


class ClinicOutPublicRoute(BaseModel):
    id: str
    doctor_id: str
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: int
    is_open: bool
    address: _ClinicAddress
    doctor: doctor_schema.DoctorOutUser

    class Config:
        orm_mode = True


class ClinicOutAdminPanel(BaseModel):
    id: str
    doctor_id: str
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: int
    is_open: bool
    address: _ClinicAddress
    doctor: doctor_schema.DoctorOut
    total_patients: int = 0
    total_appointments: int = 0
    completed_appointments: int = 0
    cancelled_appointments_by_doctor: int = 0
    cancelled_appointments_by_user: int = 0
    pending_appointments: int = 0

    class Config:
        orm_mode = True


class ClinicOutUser(BaseModel):
    id: str
    doctor_id: str
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: int
    is_open: bool
    address: _ClinicAddress
    doctor: doctor_schema.DoctorOutUser

    class Config:
        orm_mode = True
