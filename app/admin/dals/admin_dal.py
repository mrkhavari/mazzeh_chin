from app.util.crud.base import CRUDBase
from app.admin.models.admin import Admin


class AdminDAL(CRUDBase[Admin]):
    def __init__(self):
        super().__init__(model=Admin)
