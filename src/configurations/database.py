from pydantic import (
    BaseModel,
    PostgresDsn
)


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 30
    max_overflow: int = 10
