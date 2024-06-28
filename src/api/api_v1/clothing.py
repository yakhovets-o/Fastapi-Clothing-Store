from fastapi import APIRouter
import uuid
from src.schemas.clothing import ClothingSchema

router = APIRouter()

fake_clothing = [
    {'id': str(uuid.uuid4()), 'brand': 'Nike', 'name': 'vintage', 'size': 'L', 'price': 50,
     'description': 'крутая кофта'},
    {'id': str(uuid.uuid4()), 'brand': 'Adidas', 'name': 'new', 'size': 'S', 'price': 110,
     'description': 'крутая майка'}
]


@router.get('/', response_model=list[ClothingSchema])
async def get_clothing():
    return [i for i in fake_clothing]
