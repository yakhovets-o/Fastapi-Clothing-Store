from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.helpers import db_helper
from src.schemas import AccessoriesSchemaCRUD
from src.services import AccessoriesService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[AccessoriesSchemaCRUD],
)
async def get_all_accessories(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    get_all = AccessoriesService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=AccessoriesSchemaCRUD | None
)
async def get_accessories_by_id(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    get_accessories = AccessoriesService(session=session)
    result = await get_accessories.get_by_id(_id=accessories_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{accessories_id=} not found"},
        )
    return result


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=AccessoriesSchemaCRUD
)
async def create_accessories(
    accessories: AccessoriesSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_accessories = AccessoriesService(session=session)
    return await new_accessories.create(accessories=accessories)


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=dict[str, str] | None
)
async def update_accessories(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    accessories: AccessoriesSchemaCRUD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    up_accessories = AccessoriesService(session=session)
    result = await up_accessories.update(_id=accessories_id, accessories=accessories)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{accessories_id=} not found"},
        )
    return result


@router.delete(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=dict[str, str] | None
)
async def delete_accessories(
    accessories_id: Annotated[UUID4, Path(alias="id")],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    del_accessories = AccessoriesService(session=session)

    result = await del_accessories.delete(_id=accessories_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"{accessories_id=} not found"},
        )
    return result
