from fastapi import Depends
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies.redis import cache
from src.helpers import db_helper


def get_service(service):
    def _get_service(
        session: AsyncSession = Depends(db_helper.session_getter),
        redis_client: Redis = Depends(cache),
    ):
        return service(session, redis_client)

    return _get_service
