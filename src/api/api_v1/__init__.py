from fastapi import APIRouter

from src.configurations import settings

from .accessories import router as accessories_router
from .clothing import router as clothing_router
from .footwear import router as footwear_router


router = APIRouter(
    prefix=settings.api.version.v1,
)

router.include_router(
    router=clothing_router,
    prefix=settings.api.prefix.clothing,
    tags=settings.api.tags.clothing,
)

router.include_router(
    router=accessories_router,
    prefix=settings.api.prefix.accessories,
    tags=settings.api.tags.accessories,
)

router.include_router(
    router=footwear_router,
    prefix=settings.api.prefix.footwear,
    tags=settings.api.tags.footwear,
)
