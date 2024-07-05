from sqlalchemy.orm import Mapped

from src.enums import SizeAccessory

from .base import Base
from .mixins import UpdatedCreatedAtMixin, UuidPkMixin


class Accessories(Base, UuidPkMixin, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeAccessory]
    price: Mapped[int]
    description: Mapped[str]
