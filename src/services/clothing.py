from typing import Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.clothing import ClothingRepository
from src.schemas import ClothingSchemaCreate, ClothingSchemaRead, ClothingSchemaUpdate


class ClothingService:
    def __init__(self, session: AsyncSession) -> None:
        self.clothing_repository: ClothingRepository = ClothingRepository(session=session)

    async def get_all_(self) -> list[ClothingSchemaRead]:
        return await self.clothing_repository.get_all()

    async def get_by_id(self, clothing_id: UUID4) -> Optional[ClothingSchemaRead]:
        return await self.clothing_repository.get_by_id(clothing_id=clothing_id)

    async def create(self, clothing: ClothingSchemaCreate) -> ClothingSchemaRead:
        return await self.clothing_repository.create(new_clothing=clothing)

    async def update(
        self, clothing_id: UUID4, clothing: ClothingSchemaUpdate
    ) -> Optional[ClothingSchemaRead]:
        return await self.clothing_repository.update(
            clothing_id=clothing_id, update_clothing=clothing
        )

    async def delete(self, clothing_id: UUID4) -> None:
        return await self.clothing_repository.delete(clothing_id=clothing_id)
