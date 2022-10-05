from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from src.database.database import Base

class Registration(Base):
    __tablename__ = "Registration"

    team_name = Column(String, primary_key=True, index=True)
    date = Column(String)
    group_number = Column(Integer)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)

class Match(Base):
    __tablename__ = "Match"

    team_1_name = Column(String, primary_key=True, index=True)
    team_2_name = Column(String, primary_key=True, index=True)
    team_1_score = Column(Integer)
    team_2_score = Column(Integer)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)
