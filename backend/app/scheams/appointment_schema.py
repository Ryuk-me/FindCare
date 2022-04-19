from pydantic import BaseModel
from datetime import datetime
from typing import Union


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
    is_cancelled: bool
    when_cancelled: Union[datetime, None]
    created_at: datetime

    class Config:
        orm_mode = True
