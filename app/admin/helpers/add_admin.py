from typing import Optional
from fastapi import HTTPException, status

from app.admin.schemas.management import CreateAdminInputSchema, CreateAdminOutputSchema, AdminSchema, AdminRoleType
from app.admin.models.admin import Admin
from app.admin.dals.admin_dal import AdminDAL
from app.core.constant_variables import ADMIN_USERNAME_ALREADY_EXIST
from app.admin.helpers.get_hash_password import get_password_hash

async def add_admin(
    obj_in: CreateAdminInputSchema,
) -> CreateAdminOutputSchema:
    exist_admin: Optional[Admin] = await AdminDAL().get_by_username(
        username=obj_in.username
    )
    if exist_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ADMIN_USERNAME_ALREADY_EXIST,
        )
    
    admin: Admin = await AdminDAL().create(
        create_schema=AdminSchema(
            username=obj_in.username,
            password=get_password_hash(obj_in.password),
            role_type=obj_in.role_type.value,
        )
    )
    
    return CreateAdminOutputSchema(
        uid=admin.uid,
        username=admin.username,
        role_type=AdminRoleType(admin.role_type),
        time_created=admin.time_created
    )