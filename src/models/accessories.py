from datetime import datetime, timezone

from sqlalchemy.orm import Mapped

from src.utils.custom_data_types import SizeAccessories


from .base import Base
from .mixins.uuid_pk import UuidPkMixin


class Accessories(UuidPkMixin, Base):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[SizeAccessories]
    price: Mapped[int]
    description: Mapped[str]
    create_at: Mapped[datetime] = datetime.now(timezone.utc)
