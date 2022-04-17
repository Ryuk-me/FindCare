from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from app.error_handlers import errors
from fastapi.security import OAuth2PasswordBearer
from app.models import user_model, doctor_model
from app.scheams import token_schema
from app.Config import settings
from app import services as _services


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        id = payload.get("id")
        if id is None:
            raise errors.TOKEN_CREDENTIALS_ERROR
        token_data = token_schema.TokenData(id=id)
    except JWTError:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(_services.get_db)):
    token = verify_token(token)
    user = db.query(user_model.User).filter(
        user_model.User.id == token.id).first()
    if not user:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return user


def get_current_doctor(token: str = Depends(oauth2_scheme), db: Session = Depends(_services.get_db)):
    token = verify_token(token)
    doctor = db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.id == token.id).first()
    if not doctor:
        raise errors.TOKEN_CREDENTIALS_ERROR
    return doctor
