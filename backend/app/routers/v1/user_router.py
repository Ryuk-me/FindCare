from fastapi import APIRouter, Depends, status, HTTPException
from app.Config import settings
from app import services as _services
from sqlalchemy.orm import Session
from app.scheams import user_schema
from app.oauth2 import get_current_user
from app.models import user_model


router = APIRouter(
    prefix=settings.BASE_API_V1 + '/user',
    tags=['Users']
)

#! USER SIGNUP
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=user_schema.UserOut)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(_services.get_db)):
    if not _services.is_user_exist(db, user.email):
        user = _services.create_user(db, user)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exist")

#! GET CURRENT USER DETAILS
@router.get('/', status_code=status.HTTP_200_OK, response_model=user_schema.UserOut)
async def get_user_me(db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
    user = _services.get_user(db, current_user.id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'please login first')

#! GET USER BY ID (TEMPORARY ROUTE JUST TO CHECK AUTH IT WILL BE REMOVED)
# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=user_schema.UserOut)
# async def get_user(id: int, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user)):
#     user = _services.get_user(db, id)
#     if user:
#         return user
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} does not exist')
