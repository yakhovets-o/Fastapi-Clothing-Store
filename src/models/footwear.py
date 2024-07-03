from sqlalchemy.orm import Mapped

from src.enums import SizeFootwear

from .base import Base
from .mixins import UpdatedCreatedAtMixin
from .mixins import UuidPkMixin


class Footwear(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeFootwear]
    price: Mapped[int]
    description: Mapped[str]
