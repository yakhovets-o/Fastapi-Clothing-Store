import os

from dotenv import (
    find_dotenv,
    load_dotenv,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from .app import (
    ApiConfig,
    FastApiConfig,
    RunAppConfig,
)
from .database import DatabaseConfig


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(os.getenv("FASTAPI__DB__URL"),),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    run: RunAppConfig = RunAppConfig()
    fastapi: FastApiConfig = FastApiConfig()
    api: ApiConfig = ApiConfig()
    db: DatabaseConfig


settings = Settings()
