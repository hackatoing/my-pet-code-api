from fastapi import FastAPI

from app.api.routers import pets, users
from app.core.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    settings.configure_logger()

    app = FastAPI(**settings.fastapi_kwargs)
    app.include_router(users.router, prefix="/users", tags=["users"])
    app.include_router(pets.router, prefix="/pets", tags=["pets"])

    return app
