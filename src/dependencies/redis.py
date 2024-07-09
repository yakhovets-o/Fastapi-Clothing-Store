from redis.asyncio import Redis

from src.configurations import settings


async def cache() -> Redis:
    return await Redis(host=settings.redis.host, port=settings.redis.port)
