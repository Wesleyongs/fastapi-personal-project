from collections import defaultdict

import pyshorteners
import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

import src.routes.urlconversion.models as models
import src.routes.urlconversion.schemas as schemas


def get_url_conversions(db: Session):
    res = db.query(models.UrlConversion).all()
    return [i for i in res]


def delete_all_url_conversions(db: Session):
    db.execute("""DELETE FROM "UrlConversions";""")
    db.commit()
    return "Success deleted everything from db"


def create_url_conversion(db: Session, input_url: str):

    qry = (
        db.query(models.UrlConversion)
        .filter(models.UrlConversion.input_url==input_url)
        .first()
    )
    if qry is not None:
        return qry
    else:
        type_tiny = pyshorteners.Shortener()
        output_url = type_tiny.tinyurl.short(input_url)
        db_url_conversion = models.UrlConversion(
            input_url=input_url, output_url=output_url
        )        
        db.add(db_url_conversion)
        db.commit()
        db.refresh(db_url_conversion)
        return db_url_conversion
