import uvicorn

from src.api import router as api_router
from src.configurations import settings
from src.create_app import create_app


app = create_app()

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        app="app:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
