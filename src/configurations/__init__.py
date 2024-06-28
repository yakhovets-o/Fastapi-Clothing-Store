from pydantic_settings import BaseSettings

from .app import (
    RunAppConfig,
    FastApiConfig,
    ApiConfig)


class Settings(BaseSettings):
    run: RunAppConfig = RunAppConfig()
    fastapi: FastApiConfig = FastApiConfig()
    api: ApiConfig = ApiConfig()


settings = Settings()
