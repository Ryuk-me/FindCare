from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.models import doctor_model, clinic_model
from app.scheams import clinic_schema
from app.oauth2 import get_current_doctor


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/clinic',
    tags=['Clinics']
)

#! ADD A CLINIC
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=clinic_schema.ClinicOut)
async def create_clinic(clinic: clinic_schema.ClinicCreate, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor)):
    clinic = _services.add_clinic(db, clinic, current_doctor.id)
    return clinic
