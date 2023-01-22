from starlite import get


@get("/ping")
def ping() -> None:
    return
