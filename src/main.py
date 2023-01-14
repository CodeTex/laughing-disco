from starlite import LoggingConfig, Starlite, get
from .routes.data import router as data_router


@get("/")
def health_check() -> dict[str, str]:
    """Handler function for a server health check."""
    return {"action": "health-check", "result": "healthy"}


app = Starlite(
    route_handlers=[health_check, data_router],
    logging_config=LoggingConfig(
        loggers={
            "laughing-disco": {
                "level": "INFO",
                "handlers": ["queue_listener"],
            }
        }
    ),
)
