from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from app.error_handlers import errors
from fastapi.security import OAuth2PasswordBearer
from app.models import user_model, doctor_model, admin_model
from app.scheams import token_schema
from app.Config import settings
from app import services as _services
from pytz import timezone


oauth2_scheme_user = OAuth2PasswordBearer(
    tokenUrl=settings.BASE_API_V1 + '/auth/user', scheme_name="USER LOGIN")
oauth2_scheme_doctor = OAuth2PasswordBearer(
    tokenUrl=settings.BASE_API_V1 + '/auth/doctor', scheme_name="DOCTOR LOGIN")
oauth2_scheme_admin = OAuth2PasswordBearer(
    tokenUrl=settings.BASE_API_V1 + '/auth/admin', scheme_name="ADMIN LOGIN")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone('Asia/Kolkata')) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str, is_email_verification_token: bool = False, is_reset_password_token: bool = False):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        id = payload.get("id")
        if id is None:
            if is_email_verification_token:
                raise errors.VERIFICATION_LINK_EXPIRED
            if is_reset_password_token:
                raise errors.PASSWORD_RESET_LINK_EXPIRED
            raise errors.TOKEN_CREDENTIALS_ERROR
        token_data = token_schema.TokenData(**payload)
    except JWTError:
        if is_email_verification_token:
            raise errors.VERIFICATION_LINK_EXPIRED
        raise errors.TOKEN_CREDENTIALS_ERROR
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme_user), db: Session = Depends(_services.get_db)):
    token = verify_token(token)
    user = db.query(user_model.User).filter(
        user_model.User.id == token.id).first()
    if not user:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return user


def get_current_doctor(token: str = Depends(oauth2_scheme_doctor), db: Session = Depends(_services.get_db)):
    token = verify_token(token)
    doctor = db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.id == token.id).first()
    if not doctor:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return doctor


def get_current_admin(token: str = Depends(oauth2_scheme_admin), db: Session = Depends(_services.get_db)):
    token = verify_token(token)
    admin = db.query(admin_model.Admin).filter(
        admin_model.Admin.id == token.id).first()
    if not admin:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return admin
