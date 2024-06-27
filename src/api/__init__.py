from src.api.clothing import router as clothing_router


def include_router(app):
    app.include_router(clothing_router)