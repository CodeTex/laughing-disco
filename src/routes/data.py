import asyncio
import itertools
import httpx
from httpx._exceptions import HTTPStatusError
from starlite import Router, get
import logging
import operator

base_url = "https://gorest.co.in/public/v2"
logger = logging.getLogger(__name__)


async def request(session: httpx.AsyncClient, page_number: int = 1) -> list[dict]:
    res = await session.get("/users", params={"page": page_number})
    try:
        res.raise_for_status()
    except HTTPStatusError as err:
        logger.error(err)
        return []

    logger.info(f"Page {page_number} loaded.")

    return res.json()


@get("/")
async def get_all_data() -> dict[str, str]:

    async with httpx.AsyncClient(base_url=base_url) as session:
        results = await asyncio.gather(
            *[request(session=session, page_number=i) for i in range(1, 5)]
        )

    response = list(itertools.chain.from_iterable(results))
    response = sorted(response, key=operator.itemgetter("id"))

    return response


router = Router(path="/data", route_handlers=[get_all_data])
