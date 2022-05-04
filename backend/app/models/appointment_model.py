from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(String, primary_key=True, default=uuid.uuid4().hex)
    user_id = Column(String, ForeignKey(
        "users.id"
    ), nullable=False)
    doctor_id = Column(String, ForeignKey(
        "doctors.id"
    ), nullable=False)
    cid = Column(String, ForeignKey(
        "clinics.id"
    ), nullable=False)
    clinic_id = Column(String, nullable=False)
    schedule = Column(DateTime, nullable=False)
    fees_paid = Column(Boolean, server_default='False', nullable=False)
    is_completed = Column(Boolean, server_default='False', nullable=False)
    is_cancelled = Column(String, nullable=True)
    cancellation_reason = Column(String, nullable=True)
    when_cancelled = Column(DateTime, nullable=True)
    clinic = relationship('Clinic')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


#! SCHEDULE DATETIME EXAMPLE 2018-12-19 09:26:03.478039
