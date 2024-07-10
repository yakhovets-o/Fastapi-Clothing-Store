import pickle
from typing import Optional

from pydantic import UUID4
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import EntityDoesNotExistApi, EntityDoesNotExistDb
from src.repositories.clothing import ClothingRepository
from src.schemas import ClothingSchemaCreate, ClothingSchemaRead, ClothingSchemaUpdate


class ClothingService:
    def __init__(self, session: AsyncSession, redis_client: Redis) -> None:
        self.clothing_repository: ClothingRepository = ClothingRepository(session=session)
        self.redis_client = redis_client

    async def get_all_(self) -> list[ClothingSchemaRead]:
        return await self.clothing_repository.get_all()

    async def get_by_id(self, clothing_id: UUID4) -> Optional[ClothingSchemaRead]:

        if (
            cached_clothing := await self.redis_client.get(f"clothing_{clothing_id}")
        ) is not None:
            return pickle.loads(cached_clothing)
        try:
            clothing = await self.clothing_repository.get_by_id(clothing_id=clothing_id)
            await self.redis_client.set(
                f"clothing_{clothing_id}", pickle.dumps(clothing), ex=240
            )

            return clothing
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=clothing_id)

    async def create(self, clothing: ClothingSchemaCreate) -> ClothingSchemaRead:
        return await self.clothing_repository.create(new_clothing=clothing)

    async def update(
        self, clothing_id: UUID4, clothing: ClothingSchemaUpdate
    ) -> Optional[ClothingSchemaRead]:

        try:
            updated_clothing = await self.clothing_repository.update(
                clothing_id=clothing_id, update_clothing=clothing
            )
            await self.redis_client.delete(f"clothing_{clothing_id}")
            return updated_clothing
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=clothing_id)

    async def delete(self, clothing_id: UUID4) -> None:

        try:
            await self.clothing_repository.delete(clothing_id=clothing_id)
            await self.redis_client.delete(f"clothing_{clothing_id}")

        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=clothing_id)
