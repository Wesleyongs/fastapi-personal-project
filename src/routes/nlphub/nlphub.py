# Import
from fastapi import APIRouter, Depends, APIRouter, Query, Body
from sqlalchemy.orm import Session
from typing import Any, List
import pandas as pd

# Local Variables
from src.routes.nlphub import crud
from src.routes.nlphub import schemas
from src.database.database import Base, SessionLocal, engine, get_db

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/nlphub",
    tags=["nlphub"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Any)
def read_items(inputs: List[str] = Body(example=[
    "Happy Chinese new year everyone! huat ahh!!",
    "I really hate a certain select minority group",
    "The current party is doing such a terrible job, bring back donald trump!"
])) -> Any:
    """
    Retrieve items.
    """
    return crud.get_sentiments(inputs)
