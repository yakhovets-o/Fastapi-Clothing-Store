from datetime import datetime, timezone

from sqlalchemy.orm import Mapped

from .base import Base
from .mixins.uuid_pk import UuidPkMixin


class Clothing(UuidPkMixin, Base):
    brand: Mapped[str]
    name: Mapped[str]
    size: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
    create_at: Mapped[datetime] = datetime.now(timezone.utc)
