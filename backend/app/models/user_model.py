from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    profile_image = Column(
        String, nullable=True, default='https://www.pinclipart.com/picdir/middle/351-3519728_png-file-svg-default-profile-picture-free-clipart.png')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    is_superuser = Column(Boolean, server_default='FALSE', nullable=False)
