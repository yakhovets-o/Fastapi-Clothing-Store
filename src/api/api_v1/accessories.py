from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4

from src.dependencies import get_service
from src.schemas import (
    AccessorySchemaCreate,
    AccessorySchemaRead,
    AccessorySchemaUpdate,
)
from src.services import AccessoriesService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[AccessorySchemaRead],
)
async def get_all_accessories(
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))]
):
    accessories = await service.get_all_()
    return accessories


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[AccessorySchemaRead]
)
async def get_accessory_by_id(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
):
    accessory = await service.get_by_id(accessory_id=accessory_id)
    return accessory


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccessorySchemaRead)
async def create_accessory(
    accessory: AccessorySchemaCreate,
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
):
    accessory = await service.create(accessory=accessory)
    return accessory


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[AccessorySchemaRead]
)
async def update_accessory(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    accessory: AccessorySchemaUpdate,
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
):
    accessory = await service.update(accessory_id=accessory_id, accessory=accessory)
    return accessory


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_accessories(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
):
    await service.delete(accessory_id=accessory_id)
