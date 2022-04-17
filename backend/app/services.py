from app.database import SessionLocal
from app.models import user_model
from sqlalchemy.orm import Session
from app.scheams import user_schema, doctor_schema
from passlib.hash import bcrypt
from app.models import user_model, doctor_model


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#####################################################################
#! USER SERVICES


def create_user(db: Session, user: user_schema.UserCreate):
    hash = hash_password(user.password)
    user.password = hash
    user = user_model.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, id: int):
    return db.query(user_model.User).filter(
        user_model.User.id == id).first()


def is_user_exist(db: Session, email: str):
    user = db.query(user_model.User).filter(
        user_model.User.email == email).first()
    return user

#####################################################
#! DOCTOR SERVICES


def create_doctor(db: Session, doctor: doctor_schema.DoctorCreate):
    hash = hash_password(doctor.password)
    doctor.password = hash
    doctor = doctor_model.Doctor(**doctor.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def get_doctor(db: Session, id: int):
    print("hola")
    return db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.id == id).first()


def is_doctor_exist(db: Session, email: str):
    doctor = db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.email == email).first()
    return doctor


######################################################
#! PASSWORDS


def hash_password(password: str):
    return bcrypt.hash(password)


def verify_hash(password, hash):
    return bcrypt.verify(password, hash)
