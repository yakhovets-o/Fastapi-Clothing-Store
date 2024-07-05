from typing import Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.footwear import FootwearRepository
from src.schemas import FootwearSchemaCreate, FootwearSchemaRead, FootwearSchemaUpdate


class FootwearService:
    def __init__(self, session: AsyncSession) -> None:
        self.footwear_repository: FootwearRepository = FootwearRepository(session=session)

    async def get_all_(self) -> list[FootwearSchemaRead]:
        return await self.footwear_repository.get_all()

    async def get_by_id(self, footwear_id: UUID4) -> Optional[FootwearSchemaRead]:
        return await self.footwear_repository.get_by_id(footwear_id=footwear_id)

    async def create(self, footwear: FootwearSchemaCreate) -> FootwearSchemaRead:
        return await self.footwear_repository.create(new_footwear=footwear)

    async def update(
        self, footwear_id: UUID4, footwear: FootwearSchemaUpdate
    ) -> Optional[FootwearSchemaRead]:
        return await self.footwear_repository.update(
            footwear_id=footwear_id, update_footwear=footwear
        )

    async def delete(self, footwear_id: UUID4) -> None:
        return await self.footwear_repository.delete(footwear_id=footwear_id)
