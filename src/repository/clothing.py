from typing import Sequence

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import (
    delete,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Clothing
from src.schemas import (
    ClothingSchemaCRUD,
    ClothingSchemaORM,
)


class ClothingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> Sequence[ClothingSchemaORM]:
        stmt = select(Clothing)
        result = await self.session.execute(stmt)
        clothing_models = result.scalars().all()
        return paginate(
            [
                ClothingSchemaORM.model_validate(clothing_model)
                for clothing_model in clothing_models
            ]
        )

    async def get_by_id(self, _id: UUID4) -> ClothingSchemaORM | None:
        stmt = select(Clothing).where(Clothing.id == _id)
        result = await self.session.execute(stmt)
        clothing_models = result.scalar()
        if clothing_models:
            return ClothingSchemaORM.model_validate(clothing_models)
        return None

    async def create(self, new_clothing: ClothingSchemaCRUD) -> ClothingSchemaORM:
        clothing = Clothing(**new_clothing.model_dump())
        self.session.add(clothing)
        await self.session.commit()
        return ClothingSchemaORM.model_validate(clothing)

    async def update(self, _id: UUID4, update_clothing: ClothingSchemaCRUD) -> dict | None:

        stmt = select(Clothing).where(Clothing.id == _id)
        result = await self.session.execute(stmt)
        clothing_models = result.scalar()
        if not clothing_models:
            return None
        stmt = (
            update(Clothing)
            .where(Clothing.id == _id)
            .values(**update_clothing.model_dump())
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return {"message": f"the {_id} has been updated"}

    async def delete(self, _id: UUID4) -> dict | None:
        stmt = select(Clothing).where(Clothing.id == _id)
        result = await self.session.execute(stmt)
        clothing_models = result.scalar()
        if not clothing_models:
            return None

        stmt = delete(Clothing).where(Clothing.id == _id)
        await self.session.execute(stmt)
        await self.session.commit()
        return {"message": f" the {_id=} has been deleted"}
