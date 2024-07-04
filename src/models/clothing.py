from sqlalchemy.orm import Mapped

from src.enums import SizeClothing

from .base import Base
from .mixins import UpdatedCreatedAtMixin, UuidPkMixin


class Clothing(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeClothing]
    price: Mapped[int]
    description: Mapped[str]
