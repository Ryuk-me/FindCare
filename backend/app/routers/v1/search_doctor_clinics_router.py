from fastapi import APIRouter, status, Depends
from app.Config import settings
from typing import List, Optional
from app.scheams import clinic_schema
from sqlalchemy.orm import Session
from app import services as _services

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/search',
    tags=["Search"]
)


@router.get('/doctors', status_code=status.HTTP_200_OK, response_model=List[clinic_schema.ClinicOut])
async def search_doctors_clinics(city: str, speciality: Optional[str] = None, db: Session = Depends(_services.get_db)):
    city = city.capitalize()
    if speciality:
        speciality = speciality.capitalize()

    clinics = _services.search_doctor_clinics(city, speciality, db)
    return clinics
