from typing import Optional
from pydantic import BaseModel, constr
from datetime import time


class ClinicAddress(BaseModel):
    pincode: constr(max_length=6, min_length=6)
    address: str
    city: str
    state: str


class ClinicCreate(BaseModel):
    name: str
    fees: str
    session_time: str
    opens_at: time
    closes_at: time
    slots: Optional[int] = 0
    is_open: Optional[bool] = False
    address:  ClinicAddress


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
