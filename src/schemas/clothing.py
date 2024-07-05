from datetime import datetime

from pydantic import (
    UUID4,
    BaseModel,
    Field,
)

from src.enums import SizeClothing


class ClothingSchemaCreate(BaseModel):
    brand: str
    name: str
    size: SizeClothing = Field(default=None, validate_default=True)
    price: int = Field(ge=0)
    description: str

    class Config:
        from_attributes = True


class ClothingSchemaUpdate(ClothingSchemaCreate): ...


class ClothingSchemaRead(ClothingSchemaCreate):
    id: UUID4
    create_at: datetime
    updated_at: datetime
