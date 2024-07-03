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
from src.schemas import FootwearSchemaCRUD
from src.services import FootwearService

router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[FootwearSchemaCRUD])
async def get_all_footwear(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    get_all = FootwearService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get("/{id}/", response_model=FootwearSchemaCRUD)
async def get_footwear_by_id(
        footwear_id: Annotated[UUID4, Path(alias="id")],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    get_footwear = FootwearService(session=session)
    return await get_footwear.get_by_id(_id=footwear_id)


@router.post("/", response_model=FootwearSchemaCRUD)
async def create_footwear(
        footwear: FootwearSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_footwear = FootwearService(session=session)
    return await new_footwear.create(footwear=footwear)


@router.patch("/{id}/")
async def update_footwear(
        footwear_id: Annotated[UUID4, Path(alias="id")],
        footwear: FootwearSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    upd_footwear = FootwearService(session=session)
    if await upd_footwear.update(_id=footwear_id, footwear=footwear):
        return {"message": "ok"}


@router.delete("/{id}/")
async def delete_footwear(
        footwear_id: Annotated[UUID4, Path(alias="id")],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    del_footwear = FootwearService(session=session)

    return await del_footwear.delete(_id=footwear_id)
