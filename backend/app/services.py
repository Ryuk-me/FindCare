from app.database import SessionLocal
from app.models import user_model
from sqlalchemy.orm import Session
from app.scheams import user_schema, doctor_schema, clinic_schema
from passlib.hash import bcrypt
from app.models import user_model, doctor_model, clinic_model
from app.error_handlers import errors
from datetime import date, datetime


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
    user = user_model.User(age=calculate_age(user.dob), **user.dict())
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
    doctor = doctor_model.Doctor(
        age=calculate_age(doctor.dob), **doctor.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def get_doctor(db: Session, id: int):
    return db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.id == id).first()


def is_doctor_exist(db: Session, email: str):
    doctor = db.query(doctor_model.Doctor).filter(
        doctor_model.Doctor.email == email).first()
    return doctor


######################################################
#! CLINIC
def add_clinic(db: Session, clinic: clinic_schema.ClinicCreate, doctor_id: int):
    if not is_clinic_exist(db, clinic, doctor_id):
        clinic = clinic_model.Clinic(doctor_id=doctor_id, slots=calculate_slots(
            clinic.opens_at, clinic.closes_at, clinic.session_time), **clinic.dict())
        db.add(clinic)
        db.commit()
        db.refresh(clinic)
        return clinic
    raise errors.ALREADY_EXIST_CLINIC


def get_clinic(db: Session, doctor_id: int):
    clinic = db.query(clinic_model.Clinic).filter(
        clinic_model.Clinic.doctor_id == doctor_id).first()
    if clinic:
        return clinic
    raise errors.NOT_FOUND_ERROR


def is_clinic_exist(db: Session, clinic: clinic_schema.ClinicCreate, doctor_id: int):
    clinic = db.query(clinic_model.Clinic).filter(
        clinic_model.Clinic.doctor_id == doctor_id).first()
    return clinic


######################################################
#! PASSWORDS
def hash_password(password: str):
    return bcrypt.hash(password)


def verify_hash(password, hash):
    return bcrypt.verify(password, hash)


######################################################
#! UTILITY FUNCTIONS
def calculate_age(birthDate):
    today = date.today()
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


def calculate_slots(opens_at, closes_at, session_time):
    FMT = '%H:%M:%S'
    t = str(datetime.strptime(str(closes_at), FMT) -
            datetime.strptime(str(opens_at), FMT)).split(':')
    total_minutes = int(int(t[0])*60+int(t[1])*1 + int(t[2])/60)
    slots = total_minutes // int(session_time)
    return slots
