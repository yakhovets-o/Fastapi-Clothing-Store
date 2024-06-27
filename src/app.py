import uvicorn
from fastapi import FastAPI

from src.api import include_router

app = FastAPI(
    title='Clothing Store',
    description='Realization of vintage clothes'
)

include_router(app)

if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True)
