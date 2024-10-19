
from app.admin.schemas.get import AdminOutputSchema
from app.admin.models.admin import Admin
from app.admin.schemas.admin_role_type import AdminRoleType

async def get_all_admins() -> list[AdminOutputSchema]:
    admins: list[Admin] = Admin.nodes.all()
    return [AdminOutputSchema(
        uid=admin.uid,
        username=admin.username,
        role_type=AdminRoleType(admin.role_type),
        time_created=admin.time_created,
    ) for admin in admins]