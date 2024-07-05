from datetime import datetime

from pydantic import (
    UUID4,
    BaseModel,
    Field,
)

from src.enums import SizeFootwear


class FootwearSchemaCreate(BaseModel):
    brand: str
    name: str
    size: SizeFootwear
    price: int = Field(ge=0)
    description: str

    class Config:
        from_attributes = True


class FootwearSchemaUpdate(FootwearSchemaCreate): ...


class FootwearSchemaRead(FootwearSchemaCreate):
    id: UUID4
    create_at: datetime
    updated_at: datetime
