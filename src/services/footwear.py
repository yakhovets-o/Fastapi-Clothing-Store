from typing import Sequence

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.footwear import FootwearRepository
from src.schemas import (
    FootwearSchemaCRUD,
    FootwearSchemaORM,
)


class FootwearService:
    def __init__(self, session: AsyncSession) -> None:
        self.footwear_repository: FootwearRepository = FootwearRepository(session=session)

    async def get_all_(self) -> Sequence[FootwearSchemaORM]:
        return await self.footwear_repository.get_all()

    async def get_by_id(self, _id: UUID4) -> FootwearSchemaORM | None:
        return await self.footwear_repository.get_by_id(_id=_id)

    async def create(self, footwear: FootwearSchemaCRUD) -> FootwearSchemaORM:
        return await self.footwear_repository.create(new_footwear=footwear)

    async def update(
        self, _id: UUID4, footwear: FootwearSchemaCRUD
    ) -> dict[str, str] | None:
        return await self.footwear_repository.update(_id=_id, update_footwear=footwear)

    async def delete(self, _id: UUID4) -> dict[str, str] | None:
        return await self.footwear_repository.delete(_id=_id)
