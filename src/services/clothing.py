from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.clothing import ClothingRepository
from src.schemas import ClothingSchemaAddEdit


class ClothingService:
    def __init__(self, session: AsyncSession):
        self.clothing_repository = ClothingRepository(session=session)

    async def add_clothing(self, clothing: ClothingSchemaAddEdit):
        return await self.clothing_repository.add_clothing(new_clothing=clothing)