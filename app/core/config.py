from functools import lru_cache

from pydantic_settings import BaseSettings

from app.core.schemas.environment import Environment


class Settings(BaseSettings):
    APP_NAME: str = "Mazzeh Chin"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: Environment = Environment("development")
    NEO4J_URL: str = ""
    NEO4J_BOLT_URL: str = "bolt://neo4j:7687"
    NEO4J_USERNAME: str = ""
    NEO4J_PASSWORD: str = ""
    OTP_EXPIRE_MINUTES: int = 2
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = ""
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    REDIS_URL: str = "redis://redis:6379"

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
