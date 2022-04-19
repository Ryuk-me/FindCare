from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.scheams import appointment_schema
from app.oauth2 import get_current_user
from app.models import user_model


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/user/appointment',
    tags=['Appointments']
)


#! CREATE APPOINTMENT
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=appointment_schema.AppointmentOutUser)
async def create_appointment(appointment: appointment_schema.CreateAppointment, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    appointment = _services.add_appointment(db, appointment, current_user.id)
    return appointment


#! GET A LIST OF APPOINTMENTS
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[appointment_schema.AppointmentOutUser])
async def get_appointment(db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    appointment = _services.get_appointment_by_user_id(db, current_user.id)
    return appointment


#! CANCEL USER APPOINTMENT
@router.get('/cancel', status_code=status.HTTP_202_ACCEPTED)
async def delete_appointment(id: int, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    appointment = _services.get_appointment_by_id(db, id, current_user.id)
    return _services.remove_appointments(db, appointment)
