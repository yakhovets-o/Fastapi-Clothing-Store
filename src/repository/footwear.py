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

    async def get_by_id(self, _id: UUID4) -> FootwearSchemaORM | None:
        stmt = select(Footwear).where(Footwear.id == _id)
        result = await self.session.execute(stmt)
        footwear_models = result.scalar()
        if footwear_models:
            return FootwearSchemaORM.model_validate(footwear_models)
        return None

    async def create(self, new_footwear: FootwearSchemaCRUD) -> FootwearSchemaORM:
        footwear = Footwear(**new_footwear.model_dump())
        self.session.add(footwear)
        await self.session.commit()
        return FootwearSchemaORM.model_validate(footwear)

    async def update(
        self, _id: UUID4, update_footwear: FootwearSchemaCRUD
    ) -> dict[str, str] | None:
        stmt_get = select(Footwear).where(Footwear.id == _id)
        result = await self.session.execute(stmt_get)
        footwear_models = result.scalar()
        if not footwear_models:
            return None
        stmt_upd = (
            update(Footwear)
            .where(Footwear.id == _id)
            .values(**update_footwear.model_dump())
        )

        await self.session.execute(stmt_upd)
        await self.session.commit()
        return {"message": f"the {_id} has been updated"}

    async def delete(self, _id: UUID4) -> dict[str, str] | None:
        stmt_get = select(Footwear).where(Footwear.id == _id)
        result = await self.session.execute(stmt_get)
        footwear_models = result.scalar()
        if not footwear_models:
            return None

        stmt_del = delete(Footwear).where(Footwear.id == _id)

        await self.session.execute(stmt_del)
        await self.session.commit()
        return {"message": f" the {_id=} has been deleted"}
