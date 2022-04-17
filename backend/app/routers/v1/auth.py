from fastapi import Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.Config import settings
from sqlalchemy.orm import Session
from app import services as _services
from app.error_handlers import errors
from app.oauth2 import create_access_token
from app.scheams import token_schema

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/auth',
    tags=['Authentication']
)


@router.post('/user', response_model=token_schema.BaseToken)
async def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    user_exist = _services.is_user_exist(db, user_credentials.username)
    if user_exist:
        if _services.verify_hash(user_credentials.password, user_exist.password):
            token = create_access_token(data={"id": user_exist.id})
            return {"access_token": token, "token_type": "bearer"}
    raise errors.INVALID_CREDENTIALS_ERROR


@router.post('/doctor', response_model=token_schema.BaseToken)
async def doctor_login(doctor_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    doctor_exist = _services.is_doctor_exist(db, doctor_credentials.username)
    if doctor_exist:
        if _services.verify_hash(doctor_credentials.password, doctor_exist.password):
            token = create_access_token(data={"id": doctor_exist.id})
            return {"access_token": token, "token_type": "bearer"}
    raise errors.INVALID_CREDENTIALS_ERROR
