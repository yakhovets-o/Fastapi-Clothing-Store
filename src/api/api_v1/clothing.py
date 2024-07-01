from typing import Annotated

from fastapi import APIRouter, Path
from fastapi import Depends

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.clothing import ClothingSchemaAddEdit, ClothingSchema
from src.services.clothing import ClothingService
from src.bd import db_helper

router = APIRouter()

fake_clothing = [
    {'id': str(uuid.uuid4()), 'brand': 'Nike', 'name': 'vintage', 'size': 'L', 'price': 50,
     'description': 'крутая кофта'},
    {'id': str(uuid.uuid4()), 'brand': 'Adidas', 'name': 'new', 'size': 'S', 'price': 110,
     'description': 'крутая майка'}
]


@router.post('/', response_model=ClothingSchemaAddEdit)
async def add_clothing(
        clothing: ClothingSchemaAddEdit,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],):
    print(clothing)
    new_clothing = ClothingService(session=session)
    print(clothing)
    return await new_clothing.add_clothing(clothing=clothing)




