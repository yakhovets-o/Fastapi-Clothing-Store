from sqlalchemy.orm import Mapped

from src.enums import SizeAccessories

from .base import Base
from .mixins.updated_created_at import UpdatedCreatedAtMixin
from .mixins.uuid_pk import UuidPkMixin


class Accessories(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeAccessories]
    price: Mapped[int]
    description: Mapped[str]
