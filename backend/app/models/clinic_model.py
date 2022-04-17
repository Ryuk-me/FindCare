from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Time
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, JSON
from app.database import Base
from sqlalchemy.orm import relationship


class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(Integer, primary_key=True, nullable=False)
    doctor_id = Column(Integer, ForeignKey(
        "doctors.id"
    ), nullable=False, unique=True)
    name = Column(String, nullable=False)
    fees = Column(String, nullable=False)
    session_time = Column(String, nullable=False)
    opens_at = Column(Time, nullable=False)
    closes_at = Column(Time, nullable=False)
    slots = Column(Integer, nullable=False)
    is_open = Column(Boolean, server_default='False', nullable=False)
    address = Column(JSON, nullable=False)
    doctor = relationship('Doctor')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


# class ClinicAddress(Base):
#     __tablename__ = "clinics_address"
#     id = Column(Integer, primary_key=True, nullable=False)
#     clinic_id = Column(Integer, ForeignKey(
#         "clinics.id"
#     ), nullable=False)
#     pincode = Column(String(6), nullable=False)
#     address = Column(String, nullable=False)
#     city = Column(String, nullable=False)
#     state = Column(String, nullable=False)
