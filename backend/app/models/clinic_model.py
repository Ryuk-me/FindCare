from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Time
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(String, primary_key=True, default=generate_uuid)
    doctor_id = Column(String, ForeignKey(
        "doctors.id"
    ), nullable=False, unique=True)
    name = Column(String, nullable=False)
    fees = Column(String, nullable=False)
    session_time = Column(String, nullable=False)
    opens_at = Column(Time, nullable=False)
    closes_at = Column(Time, nullable=False)
    slots = Column(Integer, nullable=False)
    is_open = Column(Boolean, server_default='False', nullable=False)
    address = Column(JSONB, nullable=False)
    doctor = relationship('Doctor')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
