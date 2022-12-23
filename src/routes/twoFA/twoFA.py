# Import
from fastapi import APIRouter, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import pandas as pd

# Local Variables
from src.routes.twoFA import crud
from src.routes.twoFA import schemas
from src.database.database import Base, SessionLocal, engine, get_db

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/twoFA",
    tags=["twoFA"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def twofa(id, to_number="+6581633116", db:Session = Depends(get_db)):
    """
    1. Creates 2FA code
    2. Writes to DB
    3. Sends via SMS
    4. Return status 
    """    
    return crud.create_2FA(id, to_number, db)

@router.get("/verify")
def twofa(id, code, db:Session = Depends(get_db)):
    """
    """    
    return crud.verify_twofa(id, code, db)