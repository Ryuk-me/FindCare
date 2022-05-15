from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    profile_image = Column(String, nullable=False)
    appointments = relationship('Appointment')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    is_active = Column(Boolean, server_default='FALSE', nullable=False)
    is_banned = Column(Boolean, server_default='FALSE', nullable=False)
    when_banned = Column(DateTime, nullable=True)
