from typing import Sequence

from sqlalchemy import update, delete, select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.models import Clothing
from src.schemas import ClothingSchemaAddEdit, ClothingSchema


class ClothingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> Sequence[ClothingSchema]:
        stmt = select(Clothing)
        result = await self.session.execute(stmt)
        clothing_models = result.scalars().all()
        return [ClothingSchema.model_validate(clothing_model) for clothing_model in clothing_models]

    async def get_by_id(self, _id: UUID4) -> ClothingSchema:
        stmt = select(Clothing).where(Clothing.id == _id)
        result: Result = await self.session.execute(stmt)
        clothing_models = result.scalar()
        return ClothingSchema.model_validate(clothing_models)

    async def create(self, new_clothing: ClothingSchemaAddEdit) -> ClothingSchema:
        clothing = Clothing(**new_clothing.model_dump())
        self.session.add(clothing)
        await self.session.commit()
        return ClothingSchema.model_validate(clothing)

    async def update(self, _id: UUID4, update_clothing: ClothingSchemaAddEdit) -> None:
        stmt = update(Clothing).where(Clothing.id == _id).values(**update_clothing.model_dump())

        await self.session.execute(stmt)
        await self.session.commit()

    async def delete(self, _id: UUID4) -> None:
        print(_id)
        stmt = delete(Clothing).where(Clothing.id == _id)

        await self.session.execute(stmt)
        await self.session.commit()
