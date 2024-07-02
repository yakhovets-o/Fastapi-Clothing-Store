from sqlalchemy.orm import Mapped

from src.enums import SizeFootwear

from .base import Base
from .mixins.updated_created_at import UpdatedCreatedAtMixin
from .mixins.uuid_pk import UuidPkMixin


class Footwear(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeFootwear]
    price: Mapped[int]
    description: Mapped[str]
