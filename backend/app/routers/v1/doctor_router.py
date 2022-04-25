from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.models import doctor_model
from app.scheams import doctor_schema, change_password_schema
from app.oauth2 import get_current_doctor
from app.error_handlers import errors

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/doctor',
    tags=['Doctors']
)


# ***********************************************************************************
#! DOCTOR SIGNUP
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=doctor_schema.DoctorOut)
async def create_doctor(doctor: doctor_schema.DoctorCreate, db: Session = Depends(_services.get_db)):
    return _services.create_doctor(db, doctor)


# ***********************************************************************************
#! GET CURRENT DOCTOR I.E DOCTOR/ME
@router.get('/', status_code=status.HTTP_200_OK, response_model=doctor_schema.DoctorOut)
async def get_doctor_me(db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor)):
    return _services.get_doctor(db, current_doctor.id)


# ***********************************************************************************
#! GET CURRENT USER DETAILS WITH ALL APPOINTMENTS
@router.put('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(doctor_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor)):
    doctor = _services.get_doctor(db, current_doctor.id)
    return _services.change_password(db, doctor_p.password, doctor)
