import datetime as dt
import os

import pyotp
from dotenv import load_dotenv
from twilio.rest import Client

import src.routes.twoFA.models as models

def create_2FA(user_id,to_number, db):

    # generate 6 digit OTP
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    totp.interval = 60
    otp_code = totp.now()

    # create class
    twofa = models.TwoFA(user_id=user_id, otp_code=otp_code)

    # update or write to DB
    qry = (
        db.query(models.TwoFA)
        .filter(models.TwoFA.user_id==user_id)
    )
    if qry.first() is not None:
        qry.update({'otp_code':otp_code, 'created_date': dt.datetime.now()})
    else:
        db.add(twofa)
    db.commit()
    
    # send sms
    print(send_otp(otp_code, to_number))

    return {"status_code":"200", "message":"OTP created and sms sent"}

def verify_twofa(user_id, otp_code, db):
    
    user = db.query(models.TwoFA).get(user_id)
    
    if user.otp_code == otp_code and dt.datetime.now() - user.created_date <= dt.timedelta(seconds=60):
        return {"status_code":"200", "message":"verfied"}
    else:
        return {"status_code":"400", "message":"Invalid or expired code"}

def send_otp(otp_code, to_number="+6581633116"):
    load_dotenv()
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=otp_code,
            from_='+15139865084',
            to=to_number
        )
    return f"Message Sent to {to_number}"