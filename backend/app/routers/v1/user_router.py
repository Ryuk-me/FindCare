from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from app.Config import settings
from app import services as _services
from sqlalchemy.orm import Session
from app.scheams import user_schema
from app.oauth2 import get_current_user
from app.models import user_model
from app.scheams import change_password_schema
from app.error_handlers import errors

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/user',
    tags=['Users']
)


# ***********************************************************************************
#! USER SIGNUP
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=user_schema.UserOut)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(_services.get_db)):
    return _services.create_user(db, user)


# ***********************************************************************************
#! GET CURRENT USER DETAILS WITH ALL APPOINTMENTS
@router.get('/', status_code=status.HTTP_200_OK, response_model=user_schema.UserOut)
async def get_user_me(db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    return _services.get_user(db, current_user.id)


# ***********************************************************************************
#! CHANGE USER PASSWORD
@router.put('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(user_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    user = _services.get_user(db, current_user.id)
    return _services.change_password(db, user_p.password, user)


# ***********************************************************************************
#! UPDATE USER DETAILS
@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=user_schema.UserOut)
async def update_user_details(user: user_schema.UpdateUserDetails, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    is_something_changed: bool = False
    if user.name and user.name != current_user.name:
        current_user.name = user.name
        is_something_changed = True
    if user.email and user.email != current_user.email:
        if not _services.is_user_exist(db, user.email):
            current_user.email = user.email
            is_something_changed = True
        else:
            raise errors.EMAIL_ALREADY_EXIST
    if user.phone and user.phone != current_user.phone:
        if not _services.get_user_by_phone_no(db, user.phone):
            current_user.phone = user.phone
            is_something_changed = True
        else:
            raise errors.PHONE_NUMBER_ALREADY_EXIST
    if user.dob and user.dob != current_user.dob:
        current_user.dob = user.dob
        current_user.age = _services.calculate_age(user.dob)
        is_something_changed = True
    if user.gender and user.gender != current_user.gender:
        current_user.gender = user.gender
        is_something_changed = True
    if is_something_changed:
        current_user.updated_at = datetime.now()
        db.commit()
        return current_user
    raise errors.NOTHING_CHANGED
