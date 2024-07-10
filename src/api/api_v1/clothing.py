from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, status
from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4

from src.dependencies import get_service
from src.schemas import ClothingSchemaCreate, ClothingSchemaRead, ClothingSchemaUpdate
from src.services import ClothingService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[ClothingSchemaRead],
)
async def get_all_clothing(
    service: Annotated[ClothingService, Depends(get_service(ClothingService))]
):
    all_clothing = await service.get_all_()
    return all_clothing


add_pagination(router)


@router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[ClothingSchemaRead]
)
async def get_clothing_by_id(
    clothing_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[ClothingService, Depends(get_service(ClothingService))],
):
    clothing = await service.get_by_id(clothing_id=clothing_id)
    return clothing


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClothingSchemaRead)
async def create_clothing(
    clothing: ClothingSchemaCreate,
    service: Annotated[ClothingService, Depends(get_service(ClothingService))],
):
    clothing = await service.create(clothing=clothing)
    return clothing


@router.patch(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=Optional[ClothingSchemaRead]
)
async def update_clothing(
    clothing_id: Annotated[UUID4, Path(alias="id")],
    clothing: ClothingSchemaUpdate,
    service: Annotated[ClothingService, Depends(get_service(ClothingService))],
):
    clothing = await service.update(clothing_id=clothing_id, clothing=clothing)
    return clothing


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_clothing(
    clothing_id: Annotated[UUID4, Path(alias="id")],
    service: Annotated[ClothingService, Depends(get_service(ClothingService))],
):
    await service.delete(clothing_id=clothing_id)
