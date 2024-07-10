from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4

from src.dependencies import get_service
from src.schemas import FootwearSchemaCreate, FootwearSchemaRead, FootwearSchemaUpdate
from src.services import FootwearService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[FootwearSchemaRead],
)
async def get_all_footwear(
    service: Annotated[FootwearService, Depends(get_service(FootwearService))]
):
    all_footwear = await service.get_all_()
    return all_footwear


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[FootwearSchemaRead]
)
async def get_footwear_by_id(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[FootwearService, Depends(get_service(FootwearService))],
):
    footwear = await service.get_by_id(footwear_id=footwear_id)
    return footwear


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FootwearSchemaRead)
async def create_footwear(
    footwear: FootwearSchemaCreate,
    service: Annotated[FootwearService, Depends(get_service(FootwearService))],
):
    footwear = await service.create(footwear=footwear)
    return footwear


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[FootwearSchemaRead]
)
async def update_footwear(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    footwear: FootwearSchemaUpdate,
    service: Annotated[FootwearService, Depends(get_service(FootwearService))],
):
    footwear = await service.update(footwear_id=footwear_id, footwear=footwear)
    return footwear


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_footwear(
    footwear_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[FootwearService, Depends(get_service(FootwearService))],
):
    await service.delete(footwear_id=footwear_id)
