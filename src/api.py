import uvicorn
from starlite import LoggingConfig, Starlite

from .routes import route_handlers


app = Starlite(
    route_handlers=route_handlers,
    logging_config=LoggingConfig(
        loggers={
            "laughing-disco": {
                "level": "INFO",
                "handlers": ["queue_listener"],
            }
        }
    ),
)

if __name__ == "__main__":
    uvicorn.run(app)
