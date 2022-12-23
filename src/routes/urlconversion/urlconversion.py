#Import 
from fastapi import APIRouter, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

# Local Variables
from src.routes.urlconversion import crud
from src.routes.urlconversion import schemas
from src.database.database import Base, SessionLocal, engine

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/UrlConversion",
    tags=["UrlConversion"],
    responses={404: {"description": "Not found"}},
)

# db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/", response_model=schemas.UrlConversion, tags=["UrlConversion"]
)
def create_url_conversion(input_url, db: Session = Depends(get_db)):
    return crud.create_url_conversion(db=db, input_url=input_url)


@router.get(
    "/",
    response_model=List[schemas.UrlConversion],
    tags=["UrlConversion"],
)
def get_converted_url(db: Session = Depends(get_db)):
    return crud.get_url_conversions(db)


@router.delete("/", response_model=str, tags=["UrlConversion"])
def delete_all_url_conversions(db: Session = Depends(get_db)):
    return crud.delete_all_url_conversions(db)