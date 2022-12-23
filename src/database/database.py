from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import Settings, get_setting

SQLALCHEMY_DATABASE_URL = get_setting().db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()