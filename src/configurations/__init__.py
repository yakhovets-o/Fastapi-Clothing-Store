from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict)

from .app import (
    RunAppConfig,
    FastApiConfig,
    ApiConfig)
from .database import DatabaseConfig


class Settings(BaseSettings):
    run: RunAppConfig = RunAppConfig()
    fastapi: FastApiConfig = FastApiConfig()
    api: ApiConfig = ApiConfig()


settings = Settings()
