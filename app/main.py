from fastapi import FastAPI, HTTPException

from app.api.routers import pets, users
from app.core.errors import http_error_handler
from app.core.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    settings.configure_logger()

    app = FastAPI(**settings.fastapi_kwargs)

    # routes
    app.include_router(
        users.router, prefix=f"{settings.api_prefix}/users", tags=["users"]
    )
    app.include_router(pets.router, prefix=f"{settings.api_prefix}/pets", tags=["pets"])

    # errors
    app.add_exception_handler(HTTPException, http_error_handler)

    return app
