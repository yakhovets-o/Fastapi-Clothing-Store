from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.helpers import db_helper
from src.schemas import FootwearSchemaCRUD
from src.services import FootwearService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[FootwearSchemaCRUD],
)
async def get_all_footwear(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    get_all = FootwearService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=FootwearSchemaCRUD | None
)
async def get_footwear_by_id(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    get_footwear = FootwearService(session=session)
    result = await get_footwear.get_by_id(_id=footwear_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{footwear_id=} not found"},
        )
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FootwearSchemaCRUD)
async def create_footwear(
    footwear: FootwearSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_footwear = FootwearService(session=session)
    return await new_footwear.create(footwear=footwear)


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=dict[str, str] | None
)
async def update_footwear(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    footwear: FootwearSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    upd_footwear = FootwearService(session=session)
    result = await upd_footwear.update(_id=footwear_id, footwear=footwear)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{footwear_id=} not found"},
        )
    return result


@router.delete(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=dict[str, str] | None
)
async def delete_footwear(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    del_footwear = FootwearService(session=session)

    result = await del_footwear.delete(_id=footwear_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{footwear_id=} not found"},
        )
    return result
