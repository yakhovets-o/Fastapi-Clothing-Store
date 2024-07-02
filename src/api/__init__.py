from fastapi import APIRouter

from src.configurations import settings

from .api_v1 import router as router_api_v1


router = APIRouter()

router.include_router(router=router_api_v1, prefix=settings.api.main_prefix)
