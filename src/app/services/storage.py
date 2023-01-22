from pathlib import Path

from tinydb import Query, TinyDB

from app.models import Record


def create_db(fp: Path) -> None:
    if not fp.parent.is_dir():
        fp.mkdir(parents=False, exist_ok=False)

    if not fp.is_file():
        fp.touch(exist_ok=False)


def write(dbp: Path, data: Record):

    db = TinyDB(dbp)

    db.insert(data.dict())

    db.close()


def read(dbp: Path, line: str) -> list[Record]:

    db = TinyDB(dbp)

    Line = Query()

    raw_data = db.search(Line.line == line)

    db.close()

    data = [Record.parse_obj(record) for record in raw_data]

    return data


def read_all(dbp: Path) -> list[Record]:

    db = TinyDB(dbp)

    raw_data = db.all()

    db.close()

    data = [Record.parse_obj(record) for record in raw_data]

    return data
