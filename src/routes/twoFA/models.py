from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, DateTime
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
import datetime as dt

from src.database.database import Base

class TwoFA(Base):
    __tablename__ = 'two_fa'

    user_id = Column(Integer, primary_key=True)
    otp_code = Column(Integer)
    created_date = Column(DateTime, default=dt.datetime.now)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)
