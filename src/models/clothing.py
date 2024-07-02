from sqlalchemy.orm import Mapped
from src.enums import SizeClothing

from .base import Base
from .mixins.uuid_pk import UuidPkMixin
from .mixins.updated_created_at import UpdatedCreatedAtMixin


class Clothing(UuidPkMixin, Base, UpdatedCreatedAtMixin):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeClothing]
    price: Mapped[int]
    description: Mapped[str]
