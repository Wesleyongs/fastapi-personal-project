import datetime as dt
from typing import Optional

from pydantic import BaseModel

class Verify(BaseModel):
    status_code: int
    message: str

    class Config:
        orm_mode = True
        
class TwoFA(BaseModel):
    status_code: int
    message: str

    class Config:
        orm_mode = True