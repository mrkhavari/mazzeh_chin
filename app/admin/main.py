from fastapi import APIRouter

from app.admin.routes.login import router as login_router
from app.admin.routes.management import router as management_router


router = APIRouter(prefix="/admin", tags=["Admin"])

router.include_router(login_router)
router.include_router(management_router)