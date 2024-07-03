from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
)
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.bd import db_helper
from src.schemas.accessories import AccessoriesSchemaCRUD
from src.services.accessories import AccessoriesService


router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[AccessoriesSchemaCRUD])
async def get_all_accessories(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    get_all = AccessoriesService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get("/{id}/", response_model=AccessoriesSchemaCRUD)
async def get_accessories_by_id(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    get_accessories = AccessoriesService(session=session)
    return await get_accessories.get_by_id(_id=accessories_id)


@router.post("/", response_model=AccessoriesSchemaCRUD)
async def create_accessories(
    accessories: AccessoriesSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_accessories = AccessoriesService(session=session)
    return await new_accessories.create(accessories=accessories)


@router.patch("/{id}/")
async def update_accessories(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    accessories: AccessoriesSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    up_accessories = AccessoriesService(session=session)
    if await up_accessories.update(_id=accessories_id, accessories=accessories):
        return {"message": "ok"}


@router.delete("/{id}/")
async def delete_accessories(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    print(accessories_id)
    del_accessories = AccessoriesService(session=session)

    return await del_accessories.delete(_id=accessories_id)
