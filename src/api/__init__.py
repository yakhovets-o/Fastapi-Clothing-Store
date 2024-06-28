from fastapi import APIRouter

from src.configurations import settings

from .api_v1 import router as router_api_v1

def include_router(app):
    app.include_router(clothing_router)