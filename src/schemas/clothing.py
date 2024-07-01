from datetime import datetime

from pydantic import BaseModel, Field, UUID4

from src.utils.custom_data_types import SizeClothing


class ClothingSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeClothing
    price: int = Field(ge=0)
    description: str
    create_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ClothingSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeClothing
    price: int = Field(ge=0)
    description: str
