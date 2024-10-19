from datetime import timedelta, datetime

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.admin.models.admin import Admin
from app.admin.helpers.authenticate_admin import authenticate_admin
from app.core.config import get_settings
from app.admin.helpers.create_access_token import create_access_token
from app.admin.schemas.login import AdminLoginOutputSchema

router = APIRouter()


@router.post("/login", response_model=AdminLoginOutputSchema)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> AdminLoginOutputSchema:
    admin: Admin = await authenticate_admin(
        username=form_data.password,
        password=form_data.password,
    )
    access_token_expires = timedelta(minutes=get_settings().ADMIN_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        obj_in={"admin_id": admin.uid},
        expires_delta=access_token_expires,
    )
    return AdminLoginOutputSchema(
        access_token=access_token,
        expires_in=str(
            datetime.now() + timedelta(minutes=get_settings().ADMIN_ACCESS_TOKEN_EXPIRE_MINUTES),
        ),
    )
