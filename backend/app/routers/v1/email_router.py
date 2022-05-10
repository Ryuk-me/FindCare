from fastapi import APIRouter, Depends, status
from app.Config import settings
from app.oauth2 import verify_token
from app.error_handlers import errors
from sqlalchemy.orm import Session
from app import services as _services
from app.models import doctor_model, user_model, admin_model
from pydantic import BaseModel, EmailStr
from datetime import timedelta
from app.oauth2 import create_access_token
from app.scheams import change_password_schema

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/email',
    tags=["Email Verification"],
    redirect_slashes=False
)


class BaseEmail(BaseModel):
    email: EmailStr


class TokenResetPass(change_password_schema.ChangePassword):
    token: str


#!! IT WILL VERIFY USER MAIL ON SIGNUP
@router.get('/verify-email', status_code=status.HTTP_202_ACCEPTED)
async def verify_email(token: str, db: Session = Depends(_services.get_db)):
    token = verify_token(token, is_email_verification_token=True)
    if token.status == 'user':
        user = db.query(user_model.User).filter(
            user_model.User.id == token.id).first()
        if not user:
            raise errors.NO_USER_FOUND
        if not user.is_active:
            user.is_active = True
            db.commit()
            return {"detail": "Email verified successfully"}
        raise errors.EMAIL_ALREADY_VERIFIED
    if token.status == 'doctor':
        doctor = db.query(doctor_model.Doctor).filter(
            doctor_model.Doctor.id == token.id
        ).first()
        if not doctor:
            raise errors.DOCTOR_NOT_FOUND
        if not doctor.is_active:
            doctor.is_active = True
            db.commit()
            return {"detail": "Email verified successfully"}
        raise errors.EMAIL_ALREADY_VERIFIED


#! IT WILL SEND A RESET PASSWORD MAIL
@router.post('/reset-password', status_code=status.HTTP_202_ACCEPTED)
async def reset_password_mail(email: BaseEmail, db: Session = Depends(_services.get_db)):
    email = email.email
    user = db.query(user_model.User).filter(
        user_model.User.email == email).first()
    doctor = db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.email == email).first()
    admin = db.query(admin_model.Admin).filter(
        admin_model.Admin.email == email).first()
    if not user or doctor:
        raise errors.ACCOUNT_NOT_FOUND_WITH_THIS_EMAIL
    if admin:
        raise errors.PLEASE_CONTACT_ADMIN
    final_obj = None

    if user:
        final_obj = user
        status = 'user'
    elif doctor:
        final_obj = doctor
        status = 'doctor'

    if not final_obj.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL
    elif final_obj.is_banned:
        raise errors.USER_IS_BANNED

    expire_time = timedelta(hours=int(
        settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS))

    token = create_access_token(
        data={"id": final_obj.id, "status": status, "email": final_obj.email}, expires_delta=expire_time)

    token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

    return await _services.send_reset_password_mail(
        subject="Reset Password", recipients=final_obj.email, token_url=token_url)


#! IT WILL VERIFY USER PASSWORD RESET TOKEN
@router.get('/verify-password-reset-token', status_code=status.HTTP_202_ACCEPTED)
async def verify_password_reset_token(token: str, db: Session = Depends(_services.get_db)):
    token = verify_token(token, is_reset_password_token=True)
    if token.status == 'user':
        user = db.query(user_model.User).filter(
            user_model.User.id == token.id).first()
        if not user:
            raise errors.NO_USER_FOUND
        if not user.is_active:
            raise errors.PLEASE_VERIFY_YOUR_EMAIL
        if user.is_banned:
            raise errors.USER_IS_BANNED

    if token.status == 'doctor':
        doctor = db.query(doctor_model.Doctor).filter(
            doctor_model.Doctor.id == token.id
        ).first()

        if not doctor:
            raise errors.NO_USER_FOUND
        if not doctor.is_active:
            raise errors.PLEASE_VERIFY_YOUR_EMAIL
        if doctor.is_banned:
            raise errors.USER_IS_BANNED
    return {"detail": "Token Verified"}


#! IT WILL CHANGE PASSWORD FROM RESET TOKEN
@router.post('/change-password-from-reset-token', status_code=status.HTTP_202_ACCEPTED)
async def change_password_from_reset_token(reset_pass: TokenResetPass, db: Session = Depends(_services.get_db)):
    token = verify_token(reset_pass.token, is_reset_password_token=True)
    if token.status == 'user':
        user = db.query(user_model.User).filter(
            user_model.User.id == token.id).first()
        if not user:
            raise errors.NO_USER_FOUND
        if not user.is_active:
            raise errors.PLEASE_VERIFY_YOUR_EMAIL
        if user.is_banned:
            raise errors.USER_IS_BANNED
        return _services.change_password(db, reset_pass.password, user, user)

    if token.status == 'doctor':
        doctor = db.query(doctor_model.Doctor).filter(
            doctor_model.Doctor.id == token.id
        ).first()

        if not doctor:
            raise errors.NO_USER_FOUND
        if not doctor.is_active:
            raise errors.PLEASE_VERIFY_YOUR_EMAIL
        if doctor.is_banned:
            raise errors.USER_IS_BANNED
        return _services.change_password(db, reset_pass.password, doctor, doctor)


@router.get('/test-email', status_code=status.HTTP_202_ACCEPTED)
async def send_test_email(email, db: Session = Depends(_services.get_db)):
    return await _services.send_welcome_email(subject="Test Email", recipients=email, token="None", token_url="None")
