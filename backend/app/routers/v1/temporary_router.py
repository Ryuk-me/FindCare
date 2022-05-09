from fastapi import APIRouter, status, Depends
from app.Config import settings
from sqlalchemy.orm import Session
from app.oauth2 import get_current_admin
from app import services as _services
from app.models import admin_model, doctor_model, user_model
from app.error_handlers import errors
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/temp',
    tags=["TEMPORARY ROUTES"]
)


class User_Doctor(BaseModel):
    id: Optional[str] = None
    email: Optional[str] = None


class User(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True


@router.post('/delete/user')
async def delete_user(delete: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    if delete.id:
        user = _services.get_user(db, delete.id)
    elif delete.email:
        user = _services.is_user_exist(db, delete.email)
    if not user:
        raise errors.USER_NOT_FOUND
    db.delete(user)
    db.commit()
    return {"detail": "User deleted from db successfully"}


@router.post('/delete/doctor')
async def delete_doctor(delete: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    if delete.id:
        doctor = _services.get_doctor(db, delete.id)
    elif delete.email:
        doctor = _services.is_doctor_exist(db, delete.email)
    if not doctor:
        raise errors.DOCTOR_NOT_FOUND
    db.delete(doctor)
    db.commit()
    return {"detail": "Doctor deleted from db successfully"}


@router.get('/users', response_model=List[User])
async def get_all_users(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    users = db.query(user_model.User).all()
    if not users:
        raise errors.NO_USER_FOUND
    return users


@router.get('/doctors', response_model=List[User])
async def get_all_doctors(db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN
    doctors = db.query(doctor_model.Doctor).all()
    if not doctors:
        raise errors.DOCTOR_NOT_FOUND
    return doctors


@router.post('/verify-mail/user')
async def verify_user(verify: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN

    if verify.id:
        user = _services.get_user(db, verify.id)
    elif verify.email:
        user = _services.is_user_exist(db, verify.email)
    if not user:
        raise errors.USER_NOT_FOUND
    if user.is_active:
        raise errors.EMAIL_ALREADY_VERIFIED
    user.is_active = True
    db.commit()
    return {"detail": "User email verified successfully"}


@router.post('/verify-mail/doctor')
async def verify_doctor(verify: User_Doctor, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not current_admin.is_super_admin:
        raise errors.NOT_A_SUPER_ADMIN

    if verify.id:
        doctor = _services.get_doctor(db, verify.id)
    elif verify.email:
        doctor = _services.is_doctor_exist(db, verify.email)
    if not doctor:
        raise errors.DOCTOR_NOT_FOUND
    if doctor.is_active:
        raise errors.EMAIL_ALREADY_VERIFIED
    doctor.is_active = True
    db.commit()
    return {"detail": "Doctor email verified successfully"}
