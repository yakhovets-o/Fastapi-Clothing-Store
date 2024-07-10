import pickle
from typing import Optional

from pydantic import UUID4
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import EntityDoesNotExistApi, EntityDoesNotExistDb
from src.repositories.footwear import FootwearRepository
from src.schemas import FootwearSchemaCreate, FootwearSchemaRead, FootwearSchemaUpdate


class FootwearService:
    def __init__(self, session: AsyncSession, redis_client: Redis) -> None:
        self.footwear_repository: FootwearRepository = FootwearRepository(session=session)
        self.redis_client = redis_client

    async def get_all_(self) -> list[FootwearSchemaRead]:
        return await self.footwear_repository.get_all()

    async def get_by_id(self, footwear_id: UUID4) -> Optional[FootwearSchemaRead]:
        if (
            cached_footwear := await self.redis_client.get(f"footwear_{footwear_id}")
        ) is not None:
            return pickle.loads(cached_footwear)
        try:
            footwear = await self.footwear_repository.get_by_id(footwear_id=footwear_id)
            await self.redis_client.set(
                f"footwear_{footwear_id}", pickle.dumps(footwear), ex=240
            )

            return footwear

        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=footwear_id)

    async def create(self, footwear: FootwearSchemaCreate) -> FootwearSchemaRead:
        return await self.footwear_repository.create(new_footwear=footwear)

    async def update(
        self, footwear_id: UUID4, footwear: FootwearSchemaUpdate
    ) -> Optional[FootwearSchemaRead]:

        try:
            updated_footwear = await self.footwear_repository.update(
                footwear_id=footwear_id, update_footwear=footwear
            )
            await self.redis_client.delete(f"footwear_{footwear_id}")
            return updated_footwear
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=footwear_id)

    async def delete(self, footwear_id: UUID4) -> None:
        try:
            await self.footwear_repository.delete(footwear_id=footwear_id)
            await self.redis_client.delete(f"footwear_{footwear_id}")
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=footwear_id)
