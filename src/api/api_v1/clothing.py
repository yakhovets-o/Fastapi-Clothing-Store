from fastapi import APIRouter
import uuid

from src.schemas.clothing import ClothingSchemaAddEdit

router = APIRouter()

fake_clothing = [
    {'brand': 'Nike', 'name': 'vintage', 'size': 'L', 'price': 50,
     'description': 'крутая кофта'},
    {'brand': 'Adidas', 'name': 'new', 'size': 'S', 'price': 110,
     'description': 'крутая майка'}
]


@router.get('/', response_model=list[ClothingSchemaAddEdit])
async def get_clothing():
    return [i for i in fake_clothing]
