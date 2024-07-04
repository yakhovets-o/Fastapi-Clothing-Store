from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    HTTPException,
    status

)

from fastapi_pagination import add_pagination
from fastapi_pagination.links import LimitOffsetPage
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.bd import db_helper
from src.schemas import ClothingSchemaCRUD
from src.services import ClothingService

router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[ClothingSchemaCRUD])
async def get_all_clothing(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    get_all = ClothingService(session=session)
    return await get_all.get_all_()


add_pagination(router)


@router.get("/{id}/", response_model=ClothingSchemaCRUD | None)
async def get_clothing_by_id(
        clothing_id: Annotated[UUID4, Path(alias="id")],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    get_clothing = ClothingService(session=session)
    result = await get_clothing.get_by_id(_id=clothing_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": f"{clothing_id=} not found"})
    return result


@router.post("/", response_model=ClothingSchemaCRUD)
async def create_clothing(
        clothing: ClothingSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    new_clothing = ClothingService(session=session)
    return await new_clothing.create(clothing=clothing)


@router.patch("/{id}/")
async def update_clothing(
        clothing_id: Annotated[UUID4, Path(alias="id")],
        clothing: ClothingSchemaCRUD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    upd_clothing = ClothingService(session=session)
    result = await upd_clothing.update(_id=clothing_id, clothing=clothing)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": f"{clothing_id=} not found"})
    return result


@router.delete("/{id}/", response_model=dict | None)
async def delete_clothing(
        clothing_id: Annotated[UUID4, Path(alias="id")],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    del_clothing = ClothingService(session=session)
    result = await del_clothing.delete(_id=clothing_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": f"{clothing_id=} not found"})
    return result
