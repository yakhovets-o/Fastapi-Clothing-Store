from typing import Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.accessories import AccessoriesRepository
from src.schemas import (
    AccessorySchemaCreate,
    AccessorySchemaRead,
    AccessorySchemaUpdate,
)


class AccessoriesService:
    def __init__(self, session: AsyncSession) -> None:
        self.accessories_repository: AccessoriesRepository = AccessoriesRepository(
            session=session
        )

    async def get_all_(self) -> list[AccessorySchemaRead]:
        return await self.accessories_repository.get_all()

    async def get_by_id(self, accessory_id: UUID4) -> Optional[AccessorySchemaRead]:
        return await self.accessories_repository.get_by_id(accessory_id=accessory_id)

    async def create(self, accessory: AccessorySchemaCreate) -> AccessorySchemaRead:
        return await self.accessories_repository.create(new_accessory=accessory)

    async def update(
        self, accessory_id: UUID4, accessory: AccessorySchemaUpdate
    ) -> Optional[AccessorySchemaRead]:
        return await self.accessories_repository.update(
            accessory_id=accessory_id, update_accessory=accessory
        )

    async def delete(self, accessory_id: UUID4) -> None:
        return await self.accessories_repository.delete(accessory_id=accessory_id)
