# database
from sqlalchemy.orm import Session
import pyotp
from sqlalchemy import Column, Integer, DateTime, String
import datetime as dt
from fastapi import APIRouter, Depends, APIRouter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@itsa-dev.cwp8u9nj29mg.ap-southeast-1.rds.amazonaws.com"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# db additional


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# model

Base = declarative_base()


class TwoFA(Base):
    __tablename__ = 'twofa'

    id = Column(String, primary_key=True)
    code = Column(String)
    created_date = Column(DateTime, default=dt.datetime.now)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)


# CRUD
import os
from twilio.rest import Client
from dotenv import load_dotenv

def create_2FA(id, db):

    # generate 6digit OTP
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    totp.interval = 60
    code = totp.now()

    # create class
    twofa = TwoFA(id=id, code=code)

    # update or write to DB
    qry = (
        db.query(TwoFA)
        .filter(TwoFA.id==id)
    )
    if qry.first() is not None:
        print("Updating", qry)
        qry.update({'code':code, 'created_date': dt.datetime.now()})
    else:
        print("Creating new")
        db.add(twofa)
    db.commit()
    
    # send sms
    print(send_otp(code))

    return "Added to db"

def verify_twofa(userid, code, db):
    
    user = db.query(TwoFA).get(userid)
    
    if user.code == code and dt.datetime.now() - user.created_date <= dt.timedelta(seconds=60):
        return "Verified"
    else:
        return "incorrect or expired OTP"

def send_otp(code, to_number="+6581633116"):
    load_dotenv()
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=code,
            from_='+15139865084',
            to=to_number
        )
    return f"Message Sent to {to_number}"

