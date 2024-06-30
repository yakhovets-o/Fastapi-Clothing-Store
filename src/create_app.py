from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from configurations import settings
import bd
from src.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with bd.db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    await bd.db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
        title=settings.fastapi.title,
        description=settings.fastapi.description

    )

    return app
