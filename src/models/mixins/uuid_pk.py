from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Uuid


class UuidPkMixin:
    id: Mapped[Uuid] = mapped_column(primary_key=True)
