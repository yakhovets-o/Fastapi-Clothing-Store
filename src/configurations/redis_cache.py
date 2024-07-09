from pydantic import BaseModel


class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379
