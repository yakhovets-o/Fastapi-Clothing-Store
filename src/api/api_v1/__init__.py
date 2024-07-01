from fastapi import APIRouter

from src.configurations import settings

from .clothing import router as clothing_router

router = APIRouter(
    prefix=settings.api.version.v1,
)

router.include_router(
    router=clothing_router,
    prefix=settings.api.prefix.clothing,
    tags=settings.api.tags.clothing
)
