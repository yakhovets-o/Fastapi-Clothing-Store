import pickle
from typing import Optional

from pydantic import UUID4
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import EntityDoesNotExistApi, EntityDoesNotExistDb
from src.repositories.accessories import AccessoriesRepository
from src.schemas import (
    AccessorySchemaCreate,
    AccessorySchemaRead,
    AccessorySchemaUpdate,
)


class AccessoriesService:
    def __init__(self, session: AsyncSession, redis_client: Redis) -> None:
        self.accessories_repository: AccessoriesRepository = AccessoriesRepository(
            session=session
        )
        self.redis_client = redis_client

    async def get_all_(self) -> list[AccessorySchemaRead]:
        return await self.accessories_repository.get_all()

    async def get_by_id(self, accessory_id: UUID4) -> Optional[AccessorySchemaRead]:
        if (
            cached_accessory := await self.redis_client.get(f"accessory_{accessory_id}")
        ) is not None:
            return pickle.loads(cached_accessory)

        try:

            accessory = await self.accessories_repository.get_by_id(
                accessory_id=accessory_id
            )
            await self.redis_client.set(
                f"accessory_{accessory_id}", pickle.dumps(accessory), ex=240
            )

            return accessory
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=accessory_id)

    async def create(self, accessory: AccessorySchemaCreate) -> AccessorySchemaRead:
        return await self.accessories_repository.create(new_accessory=accessory)

    async def update(
        self, accessory_id: UUID4, accessory: AccessorySchemaUpdate
    ) -> Optional[AccessorySchemaRead]:

        try:
            updated_accessory = await self.accessories_repository.update(
                accessory_id=accessory_id, update_accessory=accessory
            )

            await self.redis_client.delete(f"accessory_{accessory_id}")

            return updated_accessory
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=accessory_id)

    async def delete(self, accessory_id: UUID4) -> None:
        try:
            await self.accessories_repository.delete(accessory_id=accessory_id)
            await self.redis_client.delete(f"accessory_{accessory_id}")
        except EntityDoesNotExistDb:
            raise EntityDoesNotExistApi(_id=accessory_id)
