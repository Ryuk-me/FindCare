from fastapi import Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.Config import settings
from sqlalchemy.orm import Session
from app import services as _services
from app.error_handlers import errors
from app.oauth2 import create_access_token
from app.scheams import token_schema
from datetime import timedelta

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/auth',
    tags=['Authentication'],
    redirect_slashes=False
)


# ***********************************************************************************
#! USER LOGIN
@router.post('/user', response_model=token_schema.BaseToken)
async def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    user_exist = _services.is_user_exist(db, user_credentials.username)
    if not user_exist:
        raise errors.ACCOUNT_NOT_FOUND_WITH_THIS_EMAIL
    if user_exist.is_banned:
        raise errors.USER_IS_BANNED
    if user_exist:
        if _services.verify_hash(user_credentials.password, user_exist.password):
            expire_time = timedelta(minutes=int(
                settings.ACCESS_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"id": user_exist.id, "email": user_exist.email, 'status': 'user', "profile_image": user_exist.profile_image}, expires_delta=expire_time)
            return {"access_token": token, "token_type": "bearer"}
    raise errors.INVALID_CREDENTIALS_ERROR


# ***********************************************************************************
#! DOCTOR LOGIN
@router.post('/doctor', response_model=token_schema.BaseToken)
async def doctor_login(doctor_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    doctor_exist = _services.is_doctor_exist(db, doctor_credentials.username)
    if not doctor_exist:
        raise errors.ACCOUNT_NOT_FOUND_WITH_THIS_EMAIL
    if doctor_exist.is_banned:
        raise errors.USER_IS_BANNED
    if doctor_exist:
        if _services.verify_hash(doctor_credentials.password, doctor_exist.password):
            expire_time = timedelta(minutes=int(
                settings.ACCESS_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"id": doctor_exist.id, "email": doctor_exist.email, 'status': 'doctor', "profile_image": doctor_exist.profile_image}, expires_delta=expire_time)
            return {"access_token": token, "token_type": "bearer"}
    raise errors.INVALID_CREDENTIALS_ERROR


# ***********************************************************************************
#! ADMIN LOGIN
@router.post('/admin', response_model=token_schema.BaseToken)
async def admin_login(admin_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    admin_exist = _services.is_admin_exist(db, admin_credentials.username)
    if not admin_exist:
        raise errors.ACCOUNT_NOT_FOUND_WITH_THIS_EMAIL
    if admin_exist:
        if _services.verify_hash(admin_credentials.password, admin_exist.password):
            expire_time = timedelta(minutes=int(
                settings.ACCESS_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"id": admin_exist.id, "email": admin_exist.email, 'status': 'admin'}, expires_delta=expire_time)
            return {"access_token": token, "token_type": "bearer"}
    raise errors.INVALID_CREDENTIALS_ERROR
