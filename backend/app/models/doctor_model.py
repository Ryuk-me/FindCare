from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base


class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    profile_image = Column(
        String, nullable=False,
        server_default='https://www.pinclipart.com/picdir/middle/351-3519728_png-file-svg-default-profile-picture-free-clipart.png')
    about = Column(String, nullable=True)
    experience_year = Column(Integer, nullable=False)
    speciality = Column(String, nullable=False)
    registration_number = Column(String, nullable=False)
    is_verified = Column(Boolean, server_default='False', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
