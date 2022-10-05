from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from src.database.database import Base

class UrlConversion(Base):
    __tablename__ = "UrlConversions"

    input_url = Column(String, primary_key=True, index=True)
    output_url = Column(String)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)


