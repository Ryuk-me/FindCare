from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.Config import settings
from app import services as _services
from app.models import doctor_model
from app.scheams import doctor_schema, change_password_schema
from app.oauth2 import get_current_doctor, create_access_token
from app.error_handlers import errors
from datetime import timedelta


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/doctor',
    tags=['Doctors'],
    redirect_slashes=False
)


# ***********************************************************************************
#! VERIFY DOCTOR STATE
def verify_doctor_state(current_doctor: doctor_model.Doctor = Depends(get_current_doctor)):
    if current_doctor.is_banned:
        raise errors.USER_IS_BANNED
    if not current_doctor.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL


# ***********************************************************************************
#! DOCTOR SIGNUP
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_doctor(doctor: doctor_schema.DoctorCreate, db: Session = Depends(_services.get_db)):
    doctor = await _services.create_doctor(db, doctor)
    expire_time = timedelta(minutes=int(
        settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(
        data={"id": doctor.id, "status": 'doctor', "email": doctor.email}, expires_delta=expire_time)
    token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

    return await _services.send_welcome_email(subject=f"Welcome to FindCare {doctor.name} !",
                                              recipients=doctor.email,
                                              token_url=token_url
                                              )


# ***********************************************************************************
#! GET CURRENT DOCTOR I.E DOCTOR/ME
@router.get('/', status_code=status.HTTP_200_OK, response_model=doctor_schema.DoctorOut)
async def get_doctor_me(db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    return _services.get_doctor(db, current_doctor.id)


# ***********************************************************************************
#! GET CURRENT USER DETAILS WITH ALL APPOINTMENTS
@router.put('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(doctor_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    doctor = _services.get_doctor(db, current_doctor.id)
    return _services.change_password(db, doctor_p.password, doctor, current_doctor)


# ***********************************************************************************
#! UPDATE USER DETAILS
@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=doctor_schema.DoctorOut)
async def update_doctor_details(doctor: doctor_schema.UpdateDoctorDetails, db: Session = Depends(_services.get_db), current_doctor: doctor_model.Doctor = Depends(get_current_doctor), access=Depends(verify_doctor_state)):
    is_something_changed: bool = False
    if doctor.phone and current_doctor.phone != doctor.phone:
        if not _services.get_doctor_by_phone_no(db, doctor.phone) and not _services.get_user_by_phone_no(db, doctor.phone):
            current_doctor.phone = doctor.phone
            is_something_changed = True
        else:
            raise errors.PHONE_NUMBER_ALREADY_EXIST
    if doctor.email and current_doctor.email != doctor.email:
        if not _services.is_doctor_exist(db, doctor.email) and not _services.is_user_exist(db, doctor.email) and not _services.is_admin_exist(db, doctor.email):
            expire_time = timedelta(minutes=int(
                settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"id": doctor.id, "status": 'doctor', "email": doctor.email}, expires_delta=expire_time)

            token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

            await _services.send_email_change(subject=f"Email Changed",
                                              recipients=doctor.email,
                                              token_url=token_url
                                              )
            current_doctor.is_active = False
            current_doctor.email = doctor.email
            is_something_changed = True
        raise errors.EMAIL_ALREADY_EXIST

    if doctor.about and current_doctor.about != doctor.about:
        current_doctor.about = doctor.about
        is_something_changed = True

    if doctor.profile_image and doctor.profile_image != current_doctor.profile_image:
        current_doctor.profile_image = doctor.profile_image
        is_something_changed = True

    if is_something_changed:
        current_doctor.updated_at = datetime.now()
        db.commit()
        return current_doctor

    raise errors.NOTHING_CHANGED
