from datetime import datetime, timezone

from pydantic import BaseModel, Field, UUID4

from src.utils.custom_data_types import SizeAccessories


class AccessoriesSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeAccessories
    price: int = Field(ge=0)
    description: str
    create_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AccessoriesSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeAccessories
    price: int = Field(ge=0)
    description: str
