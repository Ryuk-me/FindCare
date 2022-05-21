from fastapi import APIRouter, status, Depends
from app.Config import settings
from app.scheams import admin_schema, clinic_schema, change_password_schema, user_schema, doctor_schema
from sqlalchemy.orm import Session
from app import services as _services
from app.oauth2 import get_current_admin, create_access_token
from app.models import admin_model
from app.error_handlers import errors
from typing import List, Optional
from pydantic import BaseModel
from datetime import timedelta

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/admin',
    tags=["Admins"],
    redirect_slashes=False
)


class User_Doctor(BaseModel):
    id: Optional[str] = None
    email: Optional[str] = None
    new_email: str


# ***********************************************************************************
#! CREATE ADMIN (CURRENT_ADMIN MUST BE SUPER ADMIN TO CREATE OTHER ADMINS)
@router.post('/create/admin', status_code=status.HTTP_201_CREATED, response_model=admin_schema.AdminOut)
async def create_admin(admin: admin_schema.CreateAdmin, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    admin = _services.create_admin(db, admin)
    return admin


# ***********************************************************************************
#! CREATE USER BY ADMIN
@router.post('/create/user', status_code=status.HTTP_201_CREATED)
async def create_account_user(user: user_schema.AdminUserCreate, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    password = _services.generate_random_password()
    user = user_schema.UserCreate(**user.dict(), password=password)
    await _services.create_user(db, user, created_by_admin=True)
    return {"detail": "User account created successfully"}


# ***********************************************************************************
#! CREATE DOCTOR BY ADMIN
@router.post('/create/doctor', status_code=status.HTTP_201_CREATED)
async def create_account_doctor(doctor: doctor_schema.AdminDoctorCreate, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    password = _services.generate_random_password()
    doctor = doctor_schema.DoctorCreate(**doctor.dict(), password=password)
    await _services.create_doctor(db, doctor, created_by_admin=True)
    return {"detail": "Doctor account created successfully"}


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
@router.post('/doctor/verify', status_code=status.HTTP_200_OK)
async def verify_clinic(id: str, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if current_admin.is_super_admin:
        return await _services.verify_doctor(db, id)
    raise errors.NOT_A_SUPER_ADMIN


# ***********************************************************************************
#! BAN USER
@router.post('/deactivate/user', status_code=status.HTTP_200_OK)
async def deactivate_account_user(id: str, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return await _services.deactivate_account(db, id, is_user=True)


# ***********************************************************************************
#! UNBAN USER
@router.post('/activate/user', status_code=status.HTTP_200_OK)
async def activate_account_user(id: str, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return await _services.activate_account(db, id, is_user=True)


# ***********************************************************************************
#! BAN DOCTOR
@router.post('/deactivate/doctor', status_code=status.HTTP_200_OK)
async def deactivate_account_doctor(id: str, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return await _services.deactivate_account(db, id, is_user=False)


# ***********************************************************************************
#! UNBAN DOCTOR
@router.post('/activate/doctor', status_code=status.HTTP_200_OK)
async def activate_account_user(id: str, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    return await _services.activate_account(db, id, is_user=False)


# ***********************************************************************************
#! CHNAGE-USER-MAIL
@router.post('/change-mail/user', status_code=status.HTTP_200_OK)
async def change_user_mail(change_mail: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if change_mail.id:
        user = _services.get_user(db, change_mail.id)
    elif change_mail.email:
        user = _services.is_user_exist(db, change_mail.email)
    if not user:
        raise errors.USER_NOT_FOUND
    user.is_active = False
    user.email = change_mail.new_email
    db.commit()
    expire_time = timedelta(minutes=int(
        settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(
        data={"id": user.id, "status": 'user', "email": user.email}, expires_delta=expire_time)

    token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"
    await _services.send_email_change(subject=f"Email Changed",
                                      recipients=user.email,
                                      token_url=token_url
                                      )
    return {"detail": "User email changed successfully"}


# ***********************************************************************************
#! CHNAGE-DOCTOR-MAIL
@router.post('/change-mail/doctor', status_code=status.HTTP_200_OK)
async def change_doctor_mail(change_mail: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if change_mail.id:
        doctor = _services.get_doctor(db, change_mail.id)
    elif change_mail.email:
        doctor = _services.is_doctor_exist(db, change_mail.email)
    if not doctor:
        raise errors.DOCTOR_NOT_FOUND
    doctor.is_active = False
    doctor.email = change_mail.new_email
    db.commit()
    expire_time = timedelta(minutes=int(
        settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(
        data={"id": doctor.id, "status": 'doctor', "email": doctor.email}, expires_delta=expire_time)

    token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

    await _services.send_email_change(subject=f"Email Changed",
                                      recipients=doctor.email,
                                      token_url=token_url
                                      )
    return {"detail": "Doctor email changed successfully"}
