from typing import Optional

from app.admin.schemas.management import AdminDeleteOutputSchema
from app.admin.models.admin import Admin
from app.admin.dals.admin_dal import AdminDAL

async def remove_admin(
    admin_id: str,
) -> AdminDeleteOutputSchema:
    admin: Optional[Admin] = await AdminDAL().get_by_uid(
        obj_uid=admin_id
    )
    if not admin:
        return AdminDeleteOutputSchema(
            status=False,
        )
    admin.delete()
    return AdminDeleteOutputSchema(
        status=True,
    )