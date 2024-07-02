from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.repository.clothing import ClothingRepository
from src.schemas import ClothingSchemaAddEdit, ClothingSchema
from src.models import Clothing


class ClothingService:
    def __init__(self, session: AsyncSession) -> None:
        self.clothing_repository: ClothingRepository = ClothingRepository(session=session)

    async def get_all_(self) -> Sequence[ClothingSchema]:
        return await self.clothing_repository.get_all()

    async def get_by_id(self, _id: UUID4) -> ClothingSchema:
        return await self.clothing_repository.get_by_id(_id=_id)

    async def create(self, clothing: ClothingSchemaAddEdit) -> ClothingSchema:
        return await self.clothing_repository.create(new_clothing=clothing)

    async def update(self, _id: UUID4, clothing: ClothingSchemaAddEdit) -> None:
        return await self.clothing_repository.update(_id=_id, update_clothing=clothing)

    async def delete(self, _id: UUID4) -> None:
        return await self.clothing_repository.delete(_id=_id)
