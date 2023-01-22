import datetime as dt

from pydantic import BaseModel


class Record(BaseModel):

    date: dt.date = dt.date.today()
    value: float
    line: str
