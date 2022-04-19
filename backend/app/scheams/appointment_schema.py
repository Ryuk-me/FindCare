from pydantic import BaseModel
from datetime import datetime
from typing import Union
from app.scheams import clinic_schema


class BaseAppointment(BaseModel):
    clinic_id: int
    schedule: datetime
    fees_paid: bool


class CreateAppointment(BaseAppointment):
    pass


class AppointmentOut(BaseModel):
    id: int
    user_id: int
    doctor_id: int
    clinic_id: int
    schedule: datetime
    fees_paid: bool
    is_completed: bool
    is_skipped: bool
    when_skipped: Union[datetime, None]
    is_cancelled: Union[str, None]
    when_cancelled: Union[datetime, None]
    created_at: datetime

    class Config:
        orm_mode = True


class AppointmentOutUser(BaseModel):
    id: int
    user_id: int
    doctor_id: int
    clinic_id: int
    schedule: datetime
    fees_paid: bool
    is_completed: bool
    is_skipped: bool
    when_skipped: Union[datetime, None]
    is_cancelled: Union[str, None]
    when_cancelled: Union[datetime, None]
    clinic: clinic_schema.ClinicOut
    created_at: datetime

    class Config:
        orm_mode = True
