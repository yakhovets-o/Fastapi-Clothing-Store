import pickle
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4
from redis.asyncio import Redis

from src.dependencies import cache, get_service
from src.errors import EntityDoesNotExist
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
    return await service.get_all_()


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[AccessorySchemaRead]
)
async def get_accessory_by_id(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
    redis_client: Annotated[Redis, Depends(cache)],
):
    if (
        cached_accessory := await redis_client.get(f"accessory_{accessory_id}")
    ) is not None:
        return pickle.loads(cached_accessory)

    try:

        accessory = await service.get_by_id(accessory_id=accessory_id)
        await redis_client.set(
            f"accessory_{accessory_id}", pickle.dumps(accessory), ex=240
        )

        return accessory
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"{accessory_id} not found"},
        )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccessorySchemaRead)
async def create_accessory(
    accessory: AccessorySchemaCreate,
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
):
    return await service.create(accessory=accessory)


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[AccessorySchemaRead]
)
async def update_accessory(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    accessory: AccessorySchemaUpdate,
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
    redis_client: Annotated[Redis, Depends(cache)],
):
    try:
        updated_accessory = await service.update(
            accessory_id=accessory_id, accessory=accessory
        )
        await redis_client.delete(f"accessory_{accessory_id}")

        return updated_accessory
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"{accessory_id} not found"},
        )


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_accessories(
    accessory_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[AccessoriesService, Depends(get_service(AccessoriesService))],
    redis_client: Annotated[Redis, Depends(cache)],
):
    try:
        await service.delete(accessory_id=accessory_id)
        await redis_client.delete(f"accessory_{accessory_id}")
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"{accessory_id} not found"},
        )
