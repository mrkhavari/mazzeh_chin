from typing import Optional
from fastapi import HTTPException, status

from app.admin.models.admin import Admin
from app.admin.dals.admin_dal import AdminDAL
from app.admin.helpers.verify_password import verify_password
from app.core.constant_variables import INCORRECT_USERNAME_OR_PASSWORD

async def authenticate_admin(
    username: str,
    password: str,
) -> Admin:
    admin: Optional[Admin] = await AdminDAL().get_by_username(
        username=username,
    )
    if not admin or verify_password(password,admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=INCORRECT_USERNAME_OR_PASSWORD,
        )
    return admin