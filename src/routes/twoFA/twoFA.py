# Import
from fastapi import APIRouter, Depends, APIRouter, Query
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


@router.get("/", response_model=schemas.TwoFA)
def twofa(id: int = Query(default=1, description="user_id, set as 1 for this example"), to_number= Query(default="+6581633116", description="Enter your mobile here with country code, please do not spam SMS"), db: Session = Depends(get_db)):
    """
    1. Creates 2FA code
    2. Writes to DB
    3. Sends via SMS
    4. Return status 
    """
    return crud.create_2FA(id, to_number, db)


@router.get("/verify", response_model=schemas.Verify)
def twofa(code: int = Query(description="6digit OTP that was sent to your mobile"), id: int = Query(default=1, description="user_id, set as 1 for this example"), db: Session = Depends(get_db)):
    """
    Do note the OPT is only valid for 60seconds
    """
    return crud.verify_twofa(id, code, db)
