from typing import Annotated

from fastapi import APIRouter, Path
from fastapi import Depends

from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage

from pydantic import UUID4

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.clothing import ClothingSchemaCRUD
from src.services.clothing import ClothingService
from src.bd import db_helper

router = APIRouter()


@router.get('/', response_model=LimitOffsetPage[ClothingSchemaCRUD])
async def get_all_clothing(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    get_all = ClothingService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get('/{id}/', response_model=ClothingSchemaCRUD)
async def get_clothing_by_id(
        clothing_id: Annotated[UUID4, Path(alias='id')],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    get_clothing = ClothingService(session=session)
    return await get_clothing.get_by_id(_id=clothing_id)


@router.post('/', response_model=ClothingSchemaCRUD)
async def create_clothing(
        clothing: ClothingSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    new_clothing = ClothingService(session=session)
    return await new_clothing.create(clothing=clothing)


@router.patch('/{id}/')
async def update_clothing(
        clothing_id: Annotated[UUID4, Path(alias='id')],
        clothing: ClothingSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    update_clothing = ClothingService(session=session)
    if await update_clothing.update(_id=clothing_id, clothing=clothing):
        return {"message": "ok"}


@router.delete('/{id}/')
async def delete_clothing(
        clothing_id: Annotated[UUID4, Path(alias='id')],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    print(clothing_id)
    delete_clothing = ClothingService(session=session)

    return await delete_clothing.delete(_id=clothing_id)
