from typing import Optional, Literal
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime, date, time


class ClinicCreate(BaseModel):
    doctor_id: int
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: Optional[int] = 0
    is_open: Optional[bool] = False


class ClinicAddress(BaseModel):
    clinic_id: int
    pincode: constr(max_length=6, min_length=6)
    address: str
    city: str
    state: str


class ClinicOut(BaseModel):
    id: int
    doctor_id: int
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: int
    is_open: bool
    address: ClinicAddress

    class Config:
        orm_mode = True
