from fastapi import APIRouter, Depends

from app.admin.schemas.management import CreateAdminInputSchema, CreateAdminOutputSchema
from app.admin.schemas.admin_role_type import AdminRoleType
from app.admin.decorator.admin_accessibility import check_admin_accessibility
from app.admin.models.admin import Admin
from app.admin.helpers.get_current_admin import get_current_admin
from app.admin.helpers.add_admin import add_admin
from app.admin.schemas.get import AdminOutputSchema
from app.admin.helpers.get_all_admins import get_all_admins
from app.admin.helpers.get_admin_by_id import get_admin_by_id

router = APIRouter()


@router.post("/", response_model=CreateAdminOutputSchema)
@check_admin_accessibility(role_types=[AdminRoleType.SUPER_ADMIN])
async def create_admin(
    obj_in: CreateAdminInputSchema,
    admin: Admin = Depends(get_current_admin),
) -> CreateAdminOutputSchema:
    return await add_admin(
        obj_in=obj_in,
    )


@router.get("/", response_model=AdminOutputSchema)
@check_admin_accessibility(role_types=[AdminRoleType.ADMIN])
async def get_admin_info(
    admin: Admin = Depends(get_current_admin),
) -> AdminOutputSchema:
    return await get_admin_by_id(
        admin_id=admin.uid,
    )

@router.get("/all",response_model=list[AdminOutputSchema])
@check_admin_accessibility(role_types=[AdminRoleType.SUPER_ADMIN])
async def get_all(
    admin: Admin = Depends(get_current_admin),
) -> list[AdminOutputSchema]:
    return await get_all_admins()



@router.get("/{admin_id}", response_model=AdminOutputSchema)
@check_admin_accessibility(role_types=[AdminRoleType.SUPER_ADMIN])
async def get_by_id(
    admin_id: str,
    admin: Admin = Depends(get_current_admin),
) -> AdminOutputSchema:
    return await get_admin_by_id(
        admin_id=admin_id,
    )