from typing import Optional

from app.admin.schemas.get import AdminOutputSchema
from app.admin.schemas.admin_role_type import AdminRoleType
from app.admin.models.admin import Admin
from app.admin.dals.admin_dal import AdminDAL
from fastapi import status
from fastapi.exceptions import HTTPException
from app.core.constant_variables import ADMIN_NOT_FOUND

async def get_admin_by_id(
    admin_id: str,
) -> AdminOutputSchema:
    admin: Optional[Admin] = await AdminDAL().get_by_uid(obj_uid=admin_id)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ADMIN_NOT_FOUND,
        )
    return AdminOutputSchema(
        uid=admin.uid,
        username=admin.username,
        role_type=AdminRoleType(admin.role_type),
        time_created=admin.time_created,
    )