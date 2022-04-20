from app.database import SessionLocal
from app.models import user_model
from sqlalchemy.orm import Session
from app.scheams import user_schema, doctor_schema, clinic_schema, appointment_schema, admin_schema
from passlib.hash import bcrypt
from app.models import user_model, doctor_model, clinic_model, appointment_model, admin_model
from app.error_handlers import errors
from datetime import date, datetime
from app.Config import settings
import uuid


def get_db():
    db = SessionLocal()
    create_first_admin(db)
    try:
        yield db
    finally:
        db.close()


####################################################################


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
        age=calculate_age(doctor.dob), slug=generate_slug(doctor.name), **doctor.dict())
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

#! CLINIC SERVICES
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


def is_clinic_exist_by_id(db: Session, clinic_id: int):
    clinic = db.query(clinic_model.Clinic).filter(
        clinic_model.Clinic.id == clinic_id).first()
    return clinic


#####################################################

#! APPOINTMENT SERVICES
def add_appointment(db: Session, appointment: appointment_schema.CreateAppointment, user_id: int):
    clinic: clinic_schema.ClinicOut = is_clinic_exist_by_id(
        db, appointment.clinic_id)

    if clinic:
        if clinic.is_open:
            appointment = appointment_model.Appointment(
                user_id=user_id, doctor_id=clinic.doctor_id, cid=clinic.id, **appointment.dict())
            db.add(appointment)
            db.commit()
            db.refresh(appointment)
            return appointment
        raise errors.CLINIC_IS_NOT_SERVICEABLE

    raise errors.CLINIC_NOT_FOUND


def cancel_appointments(db: Session, appointment: appointment_schema.AppointmentOutUser | appointment_schema.AppointmentOut, is_User=False):
    appointment: appointment_schema.AppointmentOutUser | appointment_schema.AppointmentOut = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.id == appointment.id).first()
    if appointment.is_completed:
        raise errors.APPOINTMENT_ALREADY_COMPLETED
    if appointment.is_skipped:
        raise errors.APPOINTMENT_ALREADY_CANCELLED_BY_DR
    if appointment.is_cancelled:
        raise errors.APPOINTNEMT_ALREADY_CANCELLED
    if is_User:
        appointment.is_cancelled = 'U'
    else:
        appointment.is_cancelled = 'D'
    appointment.when_cancelled = datetime.now()
    db.commit()
    return {"detail": "appointment cancelled sucessfully"}


def skip_appointment(db: Session, appointment: appointment_schema.AppointmentOut):
    appointment: appointment_schema.AppointmentOut = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.id == appointment.id).first()
    if appointment.is_completed:
        raise errors.APPOINTMENT_ALREADY_COMPLETED
    if appointment.is_cancelled:
        raise errors.APPOINTNEMT_ALREADY_CANCELLED
    if appointment.is_skipped:
        raise errors.APPOINTMENT_ALREADY_CANCELLED_BY_DR
    appointment.is_skipped = True
    appointment.when_skipped = datetime.now()
    db.commit()
    return {"detail": "appointment skipped sucessfully"}


def appointment_completed(db: Session, appointment: appointment_schema.AppointmentOut):
    appointment: appointment_schema.AppointmentOut = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.id == appointment.id).first()
    if appointment.is_completed:
        raise errors.APPOINTMENT_ALREADY_COMPLETED
    if appointment.is_cancelled:
        raise errors.APPOINTNEMT_ALREADY_CANCELLED
    if appointment.is_skipped:
        raise errors.APPOINTMENT_ALREADY_CANCELLED_BY_DR

    appointment.is_completed = True
    db.commit()
    return {"detail": "appointment completed sucessfully"}


def get_clinic_appointments(db: Session, doctor_id: int):
    appointments = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.doctor_id == doctor_id).all()
    if appointments:
        return appointments
    raise errors.NO_APPOINTMENT_FOUND_ERROR


def get_all_appointment_by_user_id(db: Session, user_id: int):
    appointment = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.user_id == user_id).all()
    if len(appointment) > 0:
        return appointment
    raise errors.NO_APPOINTMENT_FOUND_ERROR


def get_appointment_by_user_id(db: Session, id: int, user_id: int):
    appointment = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.id == id, appointment_model.Appointment.user_id == user_id).first()
    if appointment:
        return appointment
    raise errors.NO_APPOINTMENT_FOUND_ERROR


def get_appointment_by_doctor_id(db: Session, id: int, doctor_id: int):
    appointment = db.query(appointment_model.Appointment).filter(
        appointment_model.Appointment.id == id, appointment_model.Appointment.doctor_id == doctor_id).first()
    if appointment:
        return appointment
    raise errors.NO_APPOINTMENT_FOUND_ERROR


######################################################

#! SEARCH CLINICS
def search_doctor_clinics(city: str, speciality: str | None, db: Session):
    if not speciality:
        clinic = db.query(clinic_model.Clinic).join(doctor_model.Doctor).filter(
            clinic_model.Clinic.address["city"].astext == city, doctor_model.Doctor.is_verified == True).all()
        if clinic:
            return clinic
        raise errors.NOT_FOUND_ERROR
    clinic = db.query(clinic_model.Clinic).join(doctor_model.Doctor).filter(
        clinic_model.Clinic.address["city"].astext == city, doctor_model.Doctor.speciality == speciality, doctor_model.Doctor.is_verified == True).all()
    if clinic:
        return clinic
    raise errors.NOT_FOUND_ERROR


#####################################################

#! ADMIN SERVICES
def is_admin_exist(db: Session, email: str):
    admin = db.query(admin_model.Admin).filter(
        admin_model.Admin.email == email).first()
    return admin


def create_first_admin(db: Session):
    admin = is_admin_exist(db, settings.FIRST_SUPERUSER_EMAIL)
    if not admin:
        admin_in = admin_schema.CreateAdmin(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            name=settings.FIRST_SUPERUSER_NAME,
            is_super_admin=True
        )
        admin = create_admin(db, admin_in)


def create_admin(db: Session, admin: admin_schema.CreateAdmin):
    hash = hash_password(admin.password)
    admin.password = hash
    admin = admin_model.Admin(**admin.dict())
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


######################################################

#! HASHING
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


def generate_slug(full_name: str):
    full_name = full_name.lower().split()
    full_name[0] = full_name[0].replace('.', '')
    rnd_uuid = str(uuid.uuid4())
    slug = '-'.join(full_name) + "-" + str(rnd_uuid)
    return slug


def calculate_slots(opens_at, closes_at, session_time):
    FMT = '%H:%M:%S'
    t = str(datetime.strptime(str(closes_at), FMT) -
            datetime.strptime(str(opens_at), FMT)).split(':')
    total_minutes = int(int(t[0])*60+int(t[1])*1 + int(t[2])/60)
    slots = total_minutes // int(session_time)
    return slots
