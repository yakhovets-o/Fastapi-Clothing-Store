from datetime import datetime

from pydantic import (
    UUID4,
    BaseModel,
    Field,
)

from src.enums import SizeAccessory


class AccessorySchemaCreate(BaseModel):
    brand: str
    name: str
    size: SizeAccessory
    price: int = Field(ge=0)
    description: str

    class Config:
        from_attributes = True


class AccessorySchemaUpdate(AccessorySchemaCreate): ...


class AccessorySchemaRead(AccessorySchemaCreate):
    id: UUID4
    create_at: datetime
    updated_at: datetime
