from typing import Sequence

from sqlalchemy import update, delete, select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.models import Clothing
from src.schemas import ClothingSchemaAddEdit, ClothingSchema


class ClothingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_clothing(self, new_clothing: ClothingSchemaAddEdit) -> Clothing:
        clothing = Clothing(**new_clothing.model_dump())
        self.session.add(clothing)
        await self.session.commit()
        return clothing

