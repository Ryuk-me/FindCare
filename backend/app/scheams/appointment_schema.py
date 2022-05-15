from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union
from app.scheams import clinic_schema


class BaseAppointment(BaseModel):
    clinic_id: str
    schedule: datetime
    fees_paid: bool


class CreateAppointment(BaseAppointment):
    pass


class AppointmentOut(BaseModel):
    id: str
    user_id: str
    doctor_id: str
    clinic_id: str
    schedule: datetime
    fees_paid: bool
    is_completed: bool
    cancellation_reason: Union[str, None]
    is_cancelled: Union[str, None]
    when_cancelled: Union[datetime, None]
    created_at: datetime

    class Config:
        orm_mode = True


class CancelAppointment(BaseModel):
    id: str
    cancellation_reason: Optional[str] = None


class AppointmentOutUser(BaseModel):
    id: str
    user_id: str
    doctor_id: str
    clinic_id: str
    schedule: datetime
    fees_paid: bool
    is_completed: bool
    cancellation_reason: Union[str, None]
    is_cancelled: Union[str, None]
    when_cancelled: Union[datetime, None]
    clinic: clinic_schema.ClinicOutUser
    created_at: datetime

    class Config:
        orm_mode = True
