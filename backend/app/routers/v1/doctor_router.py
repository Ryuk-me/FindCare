from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.models import doctor_model
from app.scheams import doctor_schema
from app.oauth2 import get_current_doctor

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/doctor',
    tags=['Doctors']
)


#! Doctor Signup
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=doctor_schema.DoctorOut)
async def create_doctor(doctor: doctor_schema.DoctorCreate, db: Session = Depends(_services.get_db)):
    if not _services.is_doctor_exist(db, doctor.email):
        doctor = _services.create_doctor(db, doctor)
        return doctor
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exist")


#! Get Current Doctor i.e doctor/me
@router.get('/me', status_code=status.HTTP_200_OK, response_model=doctor_schema.DoctorOut)
async def get_doctor_me(db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor)):
    doctor = _services.get_doctor(db, current_doctor.id)
    if doctor:
        return doctor
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'please login first')
