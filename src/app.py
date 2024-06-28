import uvicorn
from fastapi import FastAPI

from configurations import settings
from api import router as api_router

app = FastAPI(
    title='Clothing Store',
    description='Realization of vintage clothes'
)

include_router(app)

if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)
