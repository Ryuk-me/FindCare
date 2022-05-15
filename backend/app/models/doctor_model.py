from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    profile_image = Column(
        String, nullable=False)
    about = Column(String, nullable=True)
    experience_year = Column(Integer, nullable=False)
    speciality = Column(String, nullable=False)
    registration_number = Column(String, nullable=False, unique=True)
    is_verified = Column(Boolean, server_default='False', nullable=False)
    slug = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, server_default='FALSE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    is_banned = Column(Boolean, server_default='FALSE', nullable=False)
    when_banned = Column(DateTime, nullable=True)
