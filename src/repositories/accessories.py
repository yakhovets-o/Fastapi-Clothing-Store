from typing import Optional

from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import EntityDoesNotExist
from src.models import Accessories
from src.schemas import (
    AccessorySchemaCreate,
    AccessorySchemaRead,
    AccessorySchemaUpdate,
)


class AccessoriesRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _get_instance(self, accessory_id: UUID4) -> Optional[Accessories]:
        stmt = select(Accessories).where(Accessories.id == accessory_id)
        result = await self.session.execute(stmt)
        model = result.scalar()
        return model

    async def get_all(self) -> list[AccessorySchemaRead]:
        stmt = select(Accessories)
        result = await self.session.execute(stmt)
        accessories_models = result.scalars().all()
        return paginate(
            [
                AccessorySchemaRead.model_validate(accessories_model)
                for accessories_model in accessories_models
            ]
        )

    async def get_by_id(self, accessory_id: UUID4) -> Optional[AccessorySchemaRead]:
        accessory_model = await self._get_instance(accessory_id=accessory_id)
        if not accessory_model:
            raise EntityDoesNotExist
        return AccessorySchemaRead.model_validate(accessory_model)

    async def create(self, new_accessory: AccessorySchemaCreate) -> AccessorySchemaRead:
        accessory_model = Accessories(**new_accessory.model_dump())
        self.session.add(accessory_model)
        await self.session.commit()
        await self.session.refresh(accessory_model)

        return AccessorySchemaRead.model_validate(accessory_model)

    async def update(
        self, accessory_id: UUID4, update_accessory: AccessorySchemaUpdate
    ) -> Optional[AccessorySchemaRead]:
        accessory_model = await self._get_instance(accessory_id=accessory_id)
        if not accessory_model:
            raise EntityDoesNotExist

        accessory_data = update_accessory.model_dump(
            exclude_unset=True, exclude={"id", "create_at", "updated_at"}
        )

        for key, value in accessory_data.items():
            setattr(accessory_model, key, value)

        self.session.add(accessory_model)
        await self.session.commit()
        await self.session.refresh(accessory_model)
        return AccessorySchemaRead.model_validate(accessory_model)

    async def delete(self, accessory_id: UUID4) -> None:
        accessory_model = await self._get_instance(accessory_id=accessory_id)
        if not accessory_model:
            raise EntityDoesNotExist

        await self.session.delete(accessory_model)
        await self.session.commit()
