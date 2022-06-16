from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.exceptions.exceptions import ItemNotFound
from app.api.routers import pets, users
from app.core.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    settings.configure_logger()

    app = FastAPI(**settings.fastapi_kwargs)

    app.include_router(users.router, prefix="/users", tags=["users"])
    app.include_router(pets.router, prefix="/pets", tags=["pets"])

    @app.exception_handler(ItemNotFound)
    async def item_not_found_exception_handler(request: Request, exc: ItemNotFound):
        return JSONResponse(status_code=404, content={"detail": exc.msg})

    return app
