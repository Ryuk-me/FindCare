from fastapi import APIRouter, Depends
from app.Config import settings
from sqlalchemy.orm import Session
from app.oauth2 import get_current_admin
from app import services as _services
from app.models import admin_model, doctor_model, user_model
from app.error_handlers import errors
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
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


@router.get('/slots')
async def slot_temp(db: Session = Depends(_services.get_db)):
    slots = slot_model.Slot(appointment_details=[{
        "21-09-2002": [{
            "clinic": "Huehuehue",
            "date": "21-09-2002"
        }]
    }], clinic_id="fcc2dca8-226d-40ad-92f0-af8bd53d2fd7", doctor_id="2ce3c69a-a32a-40d6-90bb-dc4068d8732e")
    db.add(slots)
    db.commit()
    db.refresh(slots)


# @router.get('/app')
# async def get_appointmentsDateAndTimeOfAclinic(clinic_id: str, db: Session = Depends(_services.get_db)):
#     cid = clinic_id
#     appoit = db.query(appointment_model.Appointment).filter(
#         appointment_model.Appointment.clinic_id == cid).all()
#     date_and_time_list = []
#     for appointment in appoit:
#         d = datetime.fromisoformat(str(appointment.schedule))
#         which_date = f"{d:%Y-%m-%d}"
#         which_time = f"{d:%H:%M}"
#         if not date_and_time_list:
#             date_and_time_list.append(
#                 {which_date: [which_time]}
#             )
#         else:
#             for detail in date_and_time_list:
#                 if which_date in detail:
#                     list_of_num = detail[which_date]
#                     if which_time not in list_of_num:
#                         detail[which_date] = [*list_of_num, which_time]
#                     else:
#                         raise errors.TIME_SLOT_NOT_AVAILABLE
#                 else:
#                     date_and_time_list.append(
#                         {which_date: [which_time]}
#                     )
#                     break

#     return date_and_time_list
