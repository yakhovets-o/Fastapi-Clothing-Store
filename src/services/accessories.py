from typing import Sequence

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.accessories import AccessoriesRepository
from src.schemas import (
    AccessoriesSchemaCRUD,
    AccessoriesSchemaORM,
)


class AccessoriesService:
    def __init__(self, session: AsyncSession) -> None:
        self.accessories_repository: AccessoriesRepository = AccessoriesRepository(
            session=session
        )

    async def get_all_(self) -> Sequence[AccessoriesSchemaORM]:
        return await self.accessories_repository.get_all()

    async def get_by_id(self, _id: UUID4) -> AccessoriesSchemaORM:
        return await self.accessories_repository.get_by_id(_id=_id)

    async def create(self, accessories: AccessoriesSchemaCRUD) -> AccessoriesSchemaORM:
        return await self.accessories_repository.create(new_accessories=accessories)

    async def update(self, _id: UUID4, accessories: AccessoriesSchemaCRUD) -> None:
        return await self.accessories_repository.update(
            _id=_id, update_accessories=accessories
        )

    async def delete(self, _id: UUID4) -> None:
        return await self.accessories_repository.delete(_id=_id)
