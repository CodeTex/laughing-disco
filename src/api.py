from starlite import LoggingConfig, Starlite

from core import api_settings
from routes import route_handlers


app = Starlite(
    logging_config=LoggingConfig(
        loggers={
            "laughing-disco": {
                "level": api_settings.LOG_LEVEL,
                "handlers": ["queue_listener"],
            }
        }
    ),
    route_handlers=route_handlers,
)
