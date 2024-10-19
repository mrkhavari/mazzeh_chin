from typing import Optional

import jwt
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi import status
from fastapi.exceptions import HTTPException
from app.admin.dals.admin_dal import AdminDAL
from app.admin.models.admin import Admin
from app.core.config import get_settings
from app.core.constant_variables import ADMIN_NOT_FOUND

admin_oauth2_schema = OAuth2PasswordBearer(tokenUrl="admin/login")


async def get_current_admin(
    request: Request,
    token: str = Depends(admin_oauth2_schema),
) -> Admin:
    payload = jwt.decode(
        token,
        get_settings().JWT_SECRET_KEY,
        algorithms=[get_settings().JWT_ALGORITHM],
    )
    admin_id: str = str(payload.get("admin_id"))
    if admin_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ADMIN_NOT_FOUND,
        )
    admin: Optional[Admin] = await AdminDAL().get_by_uid(obj_uid=admin_id)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ADMIN_NOT_FOUND,
        )

    return admin
