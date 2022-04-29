from fastapi import APIRouter, Depends
from app.Config import settings
from app.oauth2 import verify_token
from app.error_handlers import errors
from sqlalchemy.orm import Session
from app import services as _services
from app.models import doctor_model, user_model

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/email',
    tags=["Email Verification"]
)


@router.get('/verify-email')
async def verify_email(token: str, db: Session = Depends(_services.get_db)):
    token = verify_token(token, is_email_verification_token=True)
    if not token:
        raise errors.VERIFICATION_LINK_EXPIRED
    if token.is_user:
        user = db.query(user_model.User).filter(
            user_model.User.id == token.id).first()
        if not user.is_active:
            user.is_active = True
            db.commit()
            return {"details": "email verified successfully"}
        raise errors.EMAIL_ALREADY_VERIFIED
