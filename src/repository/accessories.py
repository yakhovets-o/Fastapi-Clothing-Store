from typing import Sequence

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import (
    Result,
    delete,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Accessories
from src.schemas import (
    AccessoriesSchemaCRUD,
    AccessoriesSchemaORM,
)


class AccessoriesRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> Sequence[AccessoriesSchemaORM]:
        stmt = select(Accessories)
        result = await self.session.execute(stmt)
        accessories_models = result.scalars().all()
        return paginate(
            [
                AccessoriesSchemaORM.model_validate(accessories_model)
                for accessories_model in accessories_models
            ]
        )

    async def get_by_id(self, _id: UUID4) -> AccessoriesSchemaORM:
        stmt = select(Accessories).where(Accessories.id == _id)
        result: Result = await self.session.execute(stmt)
        accessories_models = result.scalar()
        return AccessoriesSchemaORM.model_validate(accessories_models)

    async def create(
        self, new_accessories: AccessoriesSchemaCRUD
    ) -> AccessoriesSchemaORM:
        accessories = Accessories(**new_accessories.model_dump())
        self.session.add(accessories)
        await self.session.commit()
        return AccessoriesSchemaORM.model_validate(accessories)

    async def update(self, _id: UUID4, update_accessories: AccessoriesSchemaCRUD) -> None:
        stmt = (
            update(Accessories)
            .where(Accessories.id == _id)
            .values(**update_accessories.model_dump())
        )

        await self.session.execute(stmt)
        await self.session.commit()

    async def delete(self, _id: UUID4) -> None:
        stmt = delete(Accessories).where(Accessories.id == _id)

        await self.session.execute(stmt)
        await self.session.commit()
