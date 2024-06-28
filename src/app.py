import uvicorn
from fastapi import FastAPI

from configurations import settings
from api import router as api_router

app = FastAPI(
    title=settings.fastapi.title,
    description=settings.fastapi.description

)

include_router(app)

if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)
