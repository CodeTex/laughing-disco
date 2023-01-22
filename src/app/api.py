from starlite import LoggingConfig, Starlite

from .routes import route_handlers
from .services import storage
from .settings import settings


app = Starlite(
    logging_config=LoggingConfig(
        loggers={
            "laughing-disco": {
                "level": settings.API_LOG_LEVEL,
                "handlers": ["queue_listener"],
            }
        }
    ),
    route_handlers=route_handlers,
    on_startup=[storage.create_db],
)
