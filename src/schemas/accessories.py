from datetime import datetime

from pydantic import (
    UUID4,
    BaseModel,
    Field,
)

from src.enums import SizeAccessories


class AccessoriesSchemaCRUD(BaseModel):
    brand: str
    name: str
    size: SizeAccessories
    price: int = Field(ge=0)
    description: str


class AccessoriesSchemaORM(AccessoriesSchemaCRUD):
    id: UUID4
    create_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
