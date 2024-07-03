from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.configurations import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup

    yield
    # shutdown
    print("lox")


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
        title=settings.fastapi.title,
        description=settings.fastapi.description,
    )

    return app
