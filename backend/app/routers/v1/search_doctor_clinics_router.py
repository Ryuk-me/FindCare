from fastapi import APIRouter, status, Depends
from app.Config import settings
from typing import List, Optional
from app.scheams import clinic_schema
from sqlalchemy.orm import Session
from app import services as _services

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/search',
    tags=["Search"],
    redirect_slashes=False
)


# ***********************************************************************************
#! GET ALL DOCTORS / CLINICS PUBLIC ROUTE
@router.get('/doctors', status_code=status.HTTP_200_OK, response_model=List[clinic_schema.ClinicOutPublicRoute])
async def search_doctors_clinics(city: Optional[str] = None, speciality: Optional[str] = None, db: Session = Depends(_services.get_db)):
    if city:
        city = city.capitalize()
    if speciality:
        speciality = speciality.title()

    clinics = _services.search_doctor_clinics(city, speciality, db)
    return clinics


# ***********************************************************************************
#! GET DOCTORS PROFILE
@router.get('/doctors/profile', status_code=status.HTTP_200_OK, response_model=clinic_schema.ClinicOutPublicRoute)
async def get_doctor_profile(slug: str, db: Session = Depends(_services.get_db)):
    return _services.get_doctor_profile(slug, db)
