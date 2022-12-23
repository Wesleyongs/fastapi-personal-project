import datetime as dt
from typing import Optional

from pydantic import BaseModel

class Results(BaseModel):
    team_name: str
    team_score: int
    normal_score: int
    alternate: int
    date: str
    group_number: int

    class Config:
        orm_mode = True
        
class Match(BaseModel):
    team_1_name = str
    team_1_score = int
    team_2_name = str
    team_2_score = int

    class Config:
        orm_mode = True
        
class Registration(BaseModel):
    team_name = str
    group_number = int
    date = str

    class Config:
        orm_mode = True