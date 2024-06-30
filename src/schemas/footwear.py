from datetime import datetime, timezone
from pydantic import BaseModel, Field, UUID4

from src.utils.custom_data_types import SizeFootwear


class FootwearSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeFootwear
    price: int = Field(ge=0)
    description: str
    create_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True


class FootwearSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeFootwear
    price: int = Field(ge=0)
    description: str
