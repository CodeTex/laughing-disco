import asyncio
import logging

import uvicorn

from api import app as app_api
from services.scheduler import app as app_scheduler


class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        app_scheduler.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run scheduler and the API"
    server = Server(config=uvicorn.Config(app_api, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())
    scheduler = asyncio.create_task(app_scheduler.serve())

    await asyncio.wait([scheduler, api])


if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("rocketry.task")
    logger.addHandler(logging.StreamHandler())

    asyncio.run(main())
