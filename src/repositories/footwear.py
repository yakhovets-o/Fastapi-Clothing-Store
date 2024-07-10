from typing import Optional

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import (
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import EntityDoesNotExistDb
from src.models import Footwear
from src.schemas import FootwearSchemaCreate, FootwearSchemaRead, FootwearSchemaUpdate


class FootwearRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _get_instance(self, footwear_id: UUID4) -> Optional[Footwear]:
        stmt = select(Footwear).where(Footwear.id == footwear_id)
        result = await self.session.execute(stmt)
        model = result.scalar()
        return model

    async def get_all(self) -> list[FootwearSchemaRead]:
        stmt = select(Footwear)
        result = await self.session.execute(stmt)
        footwear_models = result.scalars().all()
        return paginate(
            [
                FootwearSchemaRead.model_validate(footwear_model)
                for footwear_model in footwear_models
            ]
        )

    async def get_by_id(self, footwear_id: UUID4) -> Optional[FootwearSchemaRead]:
        footwear_model = await self._get_instance(footwear_id=footwear_id)
        if not footwear_model:
            raise EntityDoesNotExistDb
        return FootwearSchemaRead.model_validate(footwear_model)

    async def create(self, new_footwear: FootwearSchemaCreate) -> FootwearSchemaRead:
        footwear_model = Footwear(**new_footwear.model_dump())
        self.session.add(footwear_model)
        await self.session.commit()
        await self.session.refresh(footwear_model)
        return FootwearSchemaRead.model_validate(footwear_model)

    async def update(
        self, footwear_id: UUID4, update_footwear: FootwearSchemaUpdate
    ) -> Optional[FootwearSchemaRead]:
        footwear_model = await self._get_instance(footwear_id=footwear_id)
        if not footwear_model:
            raise EntityDoesNotExistDb

        footwear_data = update_footwear.model_dump(
            exclude_unset=True, exclude={"id", "create_at", "updated_at"}
        )

        for key, value in footwear_data.items():
            setattr(footwear_model, key, value)
        self.session.add(footwear_model)
        await self.session.commit()
        await self.session.refresh(footwear_model)
        return FootwearSchemaRead.model_validate(footwear_model)

    async def delete(self, footwear_id: UUID4) -> None:
        footwear_model = await self._get_instance(footwear_id=footwear_id)
        if not footwear_model:
            raise EntityDoesNotExistDb

        await self.session.delete(footwear_model)
        await self.session.commit()
