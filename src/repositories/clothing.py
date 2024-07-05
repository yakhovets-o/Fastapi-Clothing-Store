from typing import Optional

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors.errors_db import EntityDoesNotExist
from src.models import Clothing
from src.schemas import ClothingSchemaCreate, ClothingSchemaRead, ClothingSchemaUpdate


class ClothingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _get_instance(self, clothing_id: UUID4) -> Optional[Clothing]:
        stmt = select(Clothing).where(Clothing.id == clothing_id)
        result = await self.session.execute(stmt)
        model = result.scalar()
        return model

    async def get_all(self) -> list[ClothingSchemaRead]:
        stmt = select(Clothing)
        result = await self.session.execute(stmt)
        clothing_models = result.scalars().all()
        return paginate(
            [
                ClothingSchemaRead.model_validate(clothing_model)
                for clothing_model in clothing_models
            ]
        )

    async def get_by_id(self, clothing_id: UUID4) -> Optional[ClothingSchemaRead]:
        clothing_model = await self._get_instance(clothing_id=clothing_id)
        if not clothing_model:
            raise EntityDoesNotExist
        return ClothingSchemaRead.model_validate(clothing_model)

    async def create(self, new_clothing: ClothingSchemaCreate) -> ClothingSchemaRead:
        clothing_model = Clothing(**new_clothing.model_dump())
        self.session.add(clothing_model)
        await self.session.commit()
        await self.session.refresh(clothing_model)
        return ClothingSchemaRead.model_validate(clothing_model)

    async def update(
        self, clothing_id: UUID4, update_clothing: ClothingSchemaUpdate
    ) -> Optional[ClothingSchemaRead]:
        clothing_model = await self._get_instance(clothing_id=clothing_id)
        if not clothing_model:
            raise EntityDoesNotExist

        clothing_data = update_clothing.model_dump(
            exclude_unset=True, exclude={"id", "create_at", "updated_at"}
        )

        for key, value in clothing_data.items():
            setattr(clothing_model, key, value)

        self.session.add(clothing_model)
        await self.session.commit()
        await self.session.refresh(clothing_model)
        return ClothingSchemaRead.model_validate(clothing_model)

    async def delete(self, clothing_id: UUID4) -> None:

        clothing_model = await self._get_instance(clothing_id=clothing_id)
        if not clothing_model:
            raise EntityDoesNotExist

        await self.session.delete(clothing_model)
        await self.session.commit()
