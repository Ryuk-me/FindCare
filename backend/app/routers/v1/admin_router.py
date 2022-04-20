from fastapi import APIRouter, status, Depends, HTTPException
from app.Config import settings
from app.scheams import admin_schema, clinic_schema
from sqlalchemy.orm import Session
from app import services as _services
from app.oauth2 import get_current_admin
from app.models import admin_model
from app.error_handlers import errors
from typing import List


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/admin',
    tags=["Admins"]
)


# ***********************************************************************************
#! CREATE ADMIN (CURRENT_ADMIN MUST BE SUPER ADMIN TO CREATE OTHER ADMINS)
@router.post('/createadmin', status_code=status.HTTP_201_CREATED, response_model=admin_schema.AdminOut)
async def create_admin(admin: admin_schema.CreateAdmin, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not _services.is_admin_exist(db, admin.email):
        if not current_admin.is_super_admin:
            raise errors.NOT_A_SUPER_ADMIN
        admin = _services.create_admin(db, admin)
        return admin
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="admin already exist")


# ***********************************************************************************
#! GET CURRENT ADMIN
@router.get('/', status_code=status.HTTP_200_OK, response_model=admin_schema.AdminOut)
async def get_admin(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    admin = _services.get_admin_me(db, current_admin.id)
    return admin


# ***********************************************************************************
#! GET ALL CLINICS
@router.get('/clinics', status_code=status.HTTP_200_OK, response_model=List[clinic_schema.ClinicOutAdminPanel])
async def get_all_clinics(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    clinics = _services.get_all_clinics(db)
    return clinics


# ***********************************************************************************
#! VERIFY CLINICS
@router.get('/doctor/verify', status_code=status.HTTP_200_OK)
async def verify_clinic(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if current_admin.is_super_admin:
        return _services.verify_doctor(db, id)
    raise errors.NOT_A_SUPER_ADMIN
