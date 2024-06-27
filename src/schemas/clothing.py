from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field, UUID4


class SizeInternational(Enum):
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXl = 'XXL'
    XXXl = 'XXXl'
    One_size = 'One Size'


class ClothingSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeInternational
    price: int = Field(ge=0)
    description: str
    create_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True


class ClothingSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeInternational
    price: int = Field(ge=0)
    description: str
