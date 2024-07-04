from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)

from src.configurations import settings
from src.utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @classmethod  # type: ignore
    @declared_attr
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)
