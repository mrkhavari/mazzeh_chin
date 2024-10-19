from fastapi import FastAPI
from neomodel import config

from app.core.config import get_settings
from app.db.base import install_labels
from app.admin.main import router as admin_router

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(admin_router)
    return application


app: FastAPI = get_application()


@app.on_event("startup")
async def start_up():
    config.DATABASE_URL = get_settings().NEO4J_URL
    await install_labels()
