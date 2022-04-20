from fastapi import APIRouter, status, Depends, HTTPException
from app.Config import settings
from app.scheams import admin_schema
from sqlalchemy.orm import Session
from app import services as _services
from app.oauth2 import get_current_admin
from app.models import admin_model
from app.error_handlers import errors

router = APIRouter(
    prefix=settings.BASE_API_V1 + '/admin',
    tags=["Admins"]
)


@router.post('/createadmin', status_code=status.HTTP_201_CREATED, response_model=admin_schema.AdminOut)
async def create_admin(admin: admin_schema.CreateAdmin, db: Session = Depends(_services.get_db), current_admin: admin_model.Admin = Depends(get_current_admin)):
    if not _services.is_admin_exist(db, admin.email):
        if not current_admin.is_super_admin:
            raise errors.NOT_A_SUPER_ADMIN
        admin = _services.create_admin(db, admin)
        return admin
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="admin already exist")
