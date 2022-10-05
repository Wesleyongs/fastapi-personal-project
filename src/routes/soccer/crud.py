from collections import defaultdict

import datetime as dt
import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

import src.routes.soccer.models as models
import src.routes.soccer.schemas as schemas


def get_all_registrations(db: Session):
    res = db.query(models.Registration).all()
    return [i for i in res]

def get_all_matches(db: Session):
    res = db.query(models.Match).all()
    return [i for i in res]

def delete_all_registrations(db: Session):
    db.execute("""DELETE FROM "Registration";""")
    db.commit()
    return "Success deleted everything from db"

def delete_all_matches(db: Session):
    db.execute("""DELETE FROM "Match";""")
    db.commit()
    return "Success deleted everything from db"

def create_registration(db: Session, team_name: str, date: str, group_number: int):
    db_registration = models.Registration(
        team_name=team_name, date=date, group_number=group_number
    )
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

def create_match(
    db: Session,
    team_1_name: str,
    team_2_name: str,
    team_1_score: int,
    team_2_score: int,
):
    db_match = models.Match(
        team_1_name=team_1_name,
        team_2_name=team_2_name,
        team_1_score=team_1_score,
        team_2_score=team_2_score,
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match
