from sqlalchemy.orm import Mapped

from src.utils.custom_data_types import SizeFootwear

from .base import Base
from .mixins.uuid_pk import UuidPkMixin
from .mixins.updated_created_at import UpdatedCreatedAtMixin


class Footwear(UuidPkMixin, UpdatedCreatedAtMixin, Base):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeFootwear]
    price: Mapped[int]
    description: Mapped[str]
