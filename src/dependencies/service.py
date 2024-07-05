from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.helpers import db_helper


def get_service(service):
    def _get_service(session: AsyncSession = Depends(db_helper.session_getter)):
        return service(session)

    return _get_service
