from datetime import datetime, timezone
from enum import IntEnum

from pydantic import BaseModel, Field, UUID4


class SizeEU(IntEnum):
    thirty_five = 35
    thirty_six = 36
    thirty_seven = 37
    thirty_eight = 38
    thirty_nine = 39
    forty = 40
    forty_one = 41
    forty_two = 42
    forty_three = 43
    forty_four = 44
    forty_five = 45
    forty_six = 46
    forty_seven = 47
    forty_eight = 48


class FootwearSchema(BaseModel):
    id: UUID4
    brand: str
    name: str
    size: SizeEU
    price: int = Field(ge=0)
    description: str
    create_at: datetime = datetime.now(timezone.utc)

    class Config:
        from_attributes = True


class FootwearSchemaAddEdit(BaseModel):
    brand: str
    name: str
    size: SizeEU
    price: int = Field(ge=0)
    description: str
