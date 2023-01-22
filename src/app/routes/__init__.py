from starlite.router import Router

from . import health


route_handlers = [
    Router(
        path="/",
        route_handlers=[
            health.ping,
        ],
    ),
]
