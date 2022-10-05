import datetime as dt
from typing import Optional

from pydantic import BaseModel


class UrlConversion(BaseModel):
    input_url: str
    output_url: str

    class Config:
        orm_mode = True