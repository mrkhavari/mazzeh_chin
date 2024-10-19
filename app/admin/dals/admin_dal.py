from typing import Optional

from app.util.crud.base import CRUDBase
from app.admin.models.admin import Admin


class AdminDAL(CRUDBase[Admin]):
    def __init__(self):
        super().__init__(model=Admin)

    async def get_by_username(
        self,
        username: str,
    ) -> Optional[Admin]:
        admin: Optional[Admin] = Admin.nodes.get_or_none(username=username)
        return admin
