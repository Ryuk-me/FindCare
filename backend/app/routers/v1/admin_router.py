from fastapi import APIRouter, status, Depends
from app.Config import settings
from app.scheams import admin_schema, clinic_schema, change_password_schema, user_schema
from sqlalchemy.orm import Session
from app import services as _services
from app.oauth2 import get_current_admin
from app.models import admin_model
from app.error_handlers import errors
from typing import List


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/admin',
    tags=["Admins"],
    redirect_slashes=False
)


# ***********************************************************************************
#! CREATE ADMIN (CURRENT_ADMIN MUST BE SUPER ADMIN TO CREATE OTHER ADMINS)
@router.post('/createadmin', status_code=status.HTTP_201_CREATED, response_model=admin_schema.AdminOut)
async def create_admin(admin: admin_schema.CreateAdmin, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    admin = _services.create_admin(db, admin)
    return admin


# ***********************************************************************************
#! GET CURRENT ADMIN
@router.get('/', status_code=status.HTTP_200_OK, response_model=admin_schema.AdminOut)
async def get_admin(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    admin = _services.get_admin_me(db, current_admin.id)
    return admin


# ***********************************************************************************
#! CHANGE ADMIN PASSWORD
@router.put('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(admin_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    admin = _services.get_admin_me(db, current_admin.id)
    return _services.change_password(db, admin_p.password, admin, current_admin)


# ***********************************************************************************
#! GET ALL CLINICS
@router.get('/clinics', status_code=status.HTTP_200_OK, response_model=List[clinic_schema.ClinicOutAdminPanel])
async def get_all_clinics(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    clinics = _services.get_all_clinics(db)
    return clinics


# ***********************************************************************************
#! GET ALL USERS
@router.get('/users', status_code=status.HTTP_200_OK, response_model=List[user_schema.UserOutAdminPanel])
async def get_all_users(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    users = _services.get_all_users(db)
    return users


# ***********************************************************************************
#! VERIFY CLINICS
@router.get('/doctor/verify', status_code=status.HTTP_200_OK)
async def verify_clinic(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if current_admin.is_super_admin:
        return _services.verify_doctor(db, id)
    raise errors.NOT_A_SUPER_ADMIN


# ***********************************************************************************
#! BAN USER
@router.get('/deactivate/user', status_code=status.HTTP_200_OK)
async def deactivate_account_user(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return _services.deactivate_account(db, id, is_user=True)

# ***********************************************************************************
#! UNBAN USER


@router.get('/activate/user', status_code=status.HTTP_200_OK)
async def activate_account_user(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return _services.activate_account(db, id, is_user=True)


# ***********************************************************************************
#! BAN DOCTOR
@router.get('/deactivate/doctor', status_code=status.HTTP_200_OK)
async def deactivate_account_doctor(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return _services.deactivate_account(db, id, is_user=False)


# ***********************************************************************************
#! UNBAN DOCTOR
@router.get('/activate/doctor', status_code=status.HTTP_200_OK)
async def activate_account_user(id: int, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return _services.activate_account(db, id, is_user=False)
