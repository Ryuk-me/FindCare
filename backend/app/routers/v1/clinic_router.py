from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.models import doctor_model, appointment_model
from app.scheams import clinic_schema, appointment_schema
from app.oauth2 import get_current_doctor
from app.error_handlers import errors
from app.routers.v1.doctor_router import verify_doctor_state

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/doctor/clinic',
    tags=['Clinics'],
    redirect_slashes=False
)


# ***********************************************************************************
#! CREATE CLINIC
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=clinic_schema.ClinicOut)
async def create_clinic(clinic: clinic_schema.ClinicCreate, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    clinic = _services.add_clinic(db, clinic, current_doctor.id)
    return clinic


# ***********************************************************************************
#! GET CLINIC DETAILS
@router.get('/', status_code=status.HTTP_200_OK, response_model=clinic_schema.ClinicOut)
async def get_doctor_clinic(db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    clinic = _services.get_clinic(db, current_doctor.id)
    return clinic


# ***********************************************************************************
#! GET ALL APPOINTMENTS OF A CLINC
@router.get('/appointments', status_code=status.HTTP_200_OK, response_model=List[appointment_schema.AppointmentOut])
async def get_clinic_appointments(db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    appointments = _services.get_clinic_appointments(db, current_doctor.id)
    return appointments


# ***********************************************************************************
#! CANCEL A APPOINTMENT VIA DOCTOR / CLINIC
@router.get('/appointment/cancel', status_code=status.HTTP_202_ACCEPTED)
async def cancel_appointment(cancellation: appointment_schema.CancelAppointment, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    appointment = _services.get_appointment_by_doctor_id(
        db, cancellation.id, current_doctor.id)
    return _services.cancel_appointments(db, appointment, is_User=False, reason=cancellation.cancellation_reason)


# # ***********************************************************************************
#! MARK APPOINTMENT AS COMPLETED
@router.get('/appointment/completed', status_code=status.HTTP_202_ACCEPTED)
async def completed_appointment(id: str, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    appointment = _services.get_appointment_by_doctor_id(
        db, id, current_doctor.id)
    return _services.appointment_completed(db, appointment)
