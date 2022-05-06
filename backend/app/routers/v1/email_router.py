from fastapi import APIRouter, Depends, status
from app.Config import settings
from app.oauth2 import verify_token
from app.error_handlers import errors
from sqlalchemy.orm import Session
from app import services as _services
from app.models import doctor_model, user_model
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/email',
    tags=["Email Verification"],
    redirect_slashes=False
)


class BaseEmail(BaseModel):
    email: EmailStr


@router.get('/verify-email', status_code=status.HTTP_202_ACCEPTED)
async def verify_email(token: str, db: Session = Depends(_services.get_db)):
    token = verify_token(token, is_email_verification_token=True)
    if not token:
        raise errors.VERIFICATION_LINK_EXPIRED
    if token.status == 'user':
        user = db.query(user_model.User).filter(
            user_model.User.id == token.id).first()
        if not user.is_active:
            user.is_active = True
            db.commit()
            return {"details": "email verified successfully"}
        raise errors.EMAIL_ALREADY_VERIFIED
    if token.status == 'doctor':
        doctor = db.query(doctor_model.Doctor).filter(
            doctor_model.Doctor.id == token.id
        ).first()
        if not doctor.is_active:
            doctor.is_active = True
            db.commit()
            return {"details": "email verified successfully"}
        raise errors.EMAIL_ALREADY_VERIFIED


@router.post('/reset-email', status_code=status.HTTP_202_ACCEPTED)
async def reset_email(email: BaseEmail, db: Session = Depends(_services.get_db)):
    # print(email.dict())
    email = email.email
    ...


@router.get('/test-email', status_code=status.HTTP_202_ACCEPTED)
async def send_test_email(email, db: Session = Depends(_services.get_db)):
    return await _services.send_email(subject="Test Email", recipients=email, token="None", token_url="None")
    # print(email.dict())
