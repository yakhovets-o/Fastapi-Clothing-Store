from redis.asyncio import Redis  # type: ignore[import-untyped]

from src.configurations import settings


async def cache() -> Redis:
    return await Redis(host=settings.redis.host, port=settings.redis.port)
