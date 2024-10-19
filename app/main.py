from fastapi import FastAPI
from neomodel import config

from app.core.config import get_settings
from app.db.base import install_labels

def get_application() -> FastAPI:
    application = FastAPI()
    return application


app: FastAPI = get_application()


@app.on_event("startup")
async def start_up():
    config.DATABASE_URL = get_settings().NEO4J_URL
    await install_labels()
