from fastapi import APIRouter, Depends

from app.admin.schemas.management import CreateAdminInputSchema, CreateAdminOutputSchema
from app.admin.schemas.admin_role_type import AdminRoleType
from app.admin.decorator.admin_accessibility import check_admin_accessibility
from app.admin.models.admin import Admin
from app.admin.helpers.get_current_admin import get_current_admin
from app.admin.helpers.add_admin import add_admin

router = APIRouter()


@router.post("/", response_model=CreateAdminOutputSchema)
@check_admin_accessibility(role_types=[AdminRoleType.ADMIN])
async def create_admin(
    obj_in: CreateAdminInputSchema,
    admin: Admin = Depends(get_current_admin),
) -> CreateAdminOutputSchema:
    return await add_admin(
        obj_in=obj_in,
    )
