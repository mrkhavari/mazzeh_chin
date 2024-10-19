from neomodel import (
    DateTimeFormatProperty,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)

from app.admin.schemas.admin_role_type import AdminRoleType
from app.core.constant_variables import ADMIN_USERNAME_MAX_LENGTH

class Admin(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(required=True, unique_index=True, max_length=ADMIN_USERNAME_MAX_LENGTH)
    password = StringProperty(required=True)
    admin_role = StringProperty(
        choices=[(item.value, item.name) for item in AdminRoleType]
    )
    time_created = DateTimeFormatProperty(format="%Y-%m-%d %H:%M:%S", default_now=True)
