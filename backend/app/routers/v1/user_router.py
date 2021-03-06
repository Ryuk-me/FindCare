from datetime import datetime
from fastapi import APIRouter, Depends, status
from app.Config import settings
from app import services as _services
from sqlalchemy.orm import Session
from app.scheams import user_schema
from app.oauth2 import get_current_user, create_access_token
from app.models import user_model
from app.scheams import change_password_schema
from app.error_handlers import errors
from datetime import timedelta

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/user',
    tags=['Users'],
    redirect_slashes=False
)


# ***********************************************************************************
#! VERIFY USER STATE
def verify_user_state(current_user: user_model.User = Depends(get_current_user)):
    if current_user.is_banned:
        raise errors.USER_IS_BANNED
    if not current_user.is_active:
        raise errors.PLEASE_VERIFY_YOUR_EMAIL


# ***********************************************************************************
#! USER SIGNUP
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(_services.get_db)):
    user = await _services.create_user(db, user)
    expire_time = timedelta(minutes=int(
        settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(
        data={"id": user.id, "status": 'user', "email": user.email}, expires_delta=expire_time)
    # ! verification through production webiste
    token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

    return await _services.send_welcome_email(subject=f"Welcome to FindCare {user.name} !",
                                              recipients=user.email, token_url=token_url)


# ***********************************************************************************
#! GET CURRENT USER DETAILS WITH ALL APPOINTMENTS
@router.get('/', status_code=status.HTTP_200_OK, response_model=user_schema.UserOut)
async def get_user_me(db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user), access=Depends(verify_user_state)):
    return _services.get_user(db, current_user.id)


# ***********************************************************************************
#! CHANGE USER PASSWORD
@router.put('/change-password', status_code=status.HTTP_202_ACCEPTED)
async def change_password(user_p: change_password_schema.ChangePassword, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user), access=Depends(verify_user_state)):
    user = _services.get_user(db, current_user.id)
    return _services.change_password(db, user_p.password, user, current_user)


# ***********************************************************************************
#! UPDATE USER DETAILS
@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=user_schema.UserOut)
async def update_user_details(user: user_schema.UpdateUserDetails, db: Session = Depends(_services.get_db), current_user: user_model.User = Depends(get_current_user), access=Depends(verify_user_state)):
    is_something_changed: bool = False

    if user.name and user.name != current_user.name:
        current_user.name = user.name
        is_something_changed = True

    if user.phone and user.phone != current_user.phone:
        if not _services.get_user_by_phone_no(db, user.phone) and not _services.get_doctor_by_phone_no(db, user.phone):
            current_user.phone = user.phone
            is_something_changed = True
        else:
            raise errors.PHONE_NUMBER_ALREADY_EXIST

    if user.email and user.email != current_user.email:
        if not _services.is_user_exist(db, user.email) and not _services.is_doctor_exist(db, user.email) and not _services.is_admin_exist(db, user.email):
            expire_time = timedelta(minutes=int(
                settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"id": current_user.id, "status": 'user', "email": user.email}, expires_delta=expire_time)

            token_url = f"{settings.WEBSITE_HOSTED_ROOT_URL+settings.BASE_API_V1+'/verify/token/'+token}"

            await _services.send_email_change(subject=f"Email Changed",
                                              recipients=user.email,
                                              token_url=token_url
                                              )
            current_user.is_active = False
            current_user.email = user.email
            is_something_changed = True
        else:
            raise errors.EMAIL_ALREADY_EXIST

    if user.profile_image:
        current_user.profile_image = user.profile_image
        is_something_changed = True

    if is_something_changed:
        current_user.updated_at = datetime.now()
        db.commit()
        return current_user

    raise errors.NOTHING_CHANGED
