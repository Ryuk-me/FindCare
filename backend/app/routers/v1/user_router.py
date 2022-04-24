from fastapi import APIRouter, Depends, status, HTTPException
from app.Config import settings
from app import services as _services
from sqlalchemy.orm import Session
from app.scheams import user_schema
from app.oauth2 import get_current_user
from app.models import user_model
from app.scheams import change_password_schema

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
@router.post('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(user_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    user = _services.get_user(db, current_user.id)
    return _services.change_password(db, user_p.password, user)


# ***********************************************************************************
# #! UPDATE USER DETAILS
# @router.put('/', status_code=status.HTTP_202_ACCEPTED)
# async def update_user_details(user: user_schema.UpdateUserDetails, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
#     if user.name:
#         current_user.name = user.name
#     if user.email:
#         current_user.email = user.email
#     if user.phone:
#         if not _services.
#         current_user.phone = user.phone
#     user = _services.get_user(db, current_user.id)
#     return _services.change_password(db, user.password, user)
