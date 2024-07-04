from sqlalchemy.orm import Mapped

from src.enums import SizeAccessories

from .base import Base
from .mixins import UpdatedCreatedAtMixin, UuidPkMixin


class Accessories(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeAccessories]
    price: Mapped[int]
    description: Mapped[str]
