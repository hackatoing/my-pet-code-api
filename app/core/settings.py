import logging
import sys
from functools import lru_cache
from typing import Any, Dict, Tuple

from loguru import logger
from pydantic import BaseSettings, PostgresDsn

from app.core.logging import InterceptHandler


class Settings(BaseSettings):
    # general info
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "My Pet Code"
    version: str = "0.1.0"

    # database
    database_url: PostgresDsn

    # logging
    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.error", "uvicorn.access")

    api_prefix: str = "/api"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logger(self) -> None:
        """
        Configure logger
        """
        logging.getLogger().handlers.clear()
        logging.getLogger().handlers = [InterceptHandler()]

        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]
            logging_logger.propagate = False

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])


@lru_cache
def get_settings() -> Settings:
    return Settings()
