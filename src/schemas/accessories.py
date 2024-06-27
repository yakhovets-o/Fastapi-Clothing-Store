from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, Field, UUID4


class SizeAccessories(Enum):
    One_size = 'One Size'


class AccessoriesSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeAccessories
    price: int = Field(ge=0)
    description: str
    create_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True


class AccessoriesSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeAccessories
    price: int = Field(ge=0)
    description: str
