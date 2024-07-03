from typing import Sequence

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import (
    delete,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Footwear
from src.schemas import (
    FootwearSchemaCRUD,
    FootwearSchemaORM,
)


class FootwearRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> Sequence[FootwearSchemaORM]:
        stmt = select(Footwear)
        result = await self.session.execute(stmt)
        footwear_models = result.scalars().all()
        return paginate(
            [
                FootwearSchemaORM.model_validate(footwear_model)
                for footwear_model in footwear_models
            ]
        )

    async def get_by_id(self, _id: UUID4) -> FootwearSchemaORM:
        stmt = select(Footwear).where(Footwear.id == _id)
        result = await self.session.execute(stmt)
        footwear_models = result.scalar()
        return FootwearSchemaORM.model_validate(footwear_models)

    async def create(self, new_footwear: FootwearSchemaCRUD) -> FootwearSchemaORM:
        footwear = Footwear(**new_footwear.model_dump())
        self.session.add(footwear)
        await self.session.commit()
        return FootwearSchemaORM.model_validate(footwear)

    async def update(self, _id: UUID4, update_footwear: FootwearSchemaCRUD) -> None:
        stmt = (
            update(Footwear)
            .where(Footwear.id == _id)
            .values(**update_footwear.model_dump())
        )

        await self.session.execute(stmt)
        await self.session.commit()

    async def delete(self, _id: UUID4) -> None:
        stmt = delete(Footwear).where(Footwear.id == _id)

        await self.session.execute(stmt)
        await self.session.commit()
