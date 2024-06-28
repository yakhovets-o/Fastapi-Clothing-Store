from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict)

from .app import (
    RunAppConfig,
    FastApiConfig,
    ApiConfig)
from .database import DatabaseConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env',),
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='FASTAPI__'

    )
    run: RunAppConfig = RunAppConfig()
    fastapi: FastApiConfig = FastApiConfig()
    api: ApiConfig = ApiConfig()


settings = Settings()
