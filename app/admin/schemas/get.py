from dataclasses import dataclass

from app.admin.schemas.admin_role_type import AdminRoleType

@dataclass
class AdminOutputSchema:
    uid: str
    username: str
    role_type: AdminRoleType
    time_created: str