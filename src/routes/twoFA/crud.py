import datetime as dt
import os

import pyotp
from dotenv import load_dotenv
from twilio.rest import Client

import src.routes.twoFA.models as models

load_dotenv()

def register_twillio_number(phone_number):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    validation_request = client.validation_requests \
        .create(
            friendly_name=str(phone_number),
            phone_number=phone_number
        )
    return validation_request.phone_number


def create_2FA(user_id, to_number, db):
    
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
        .filter(models.TwoFA.user_id == user_id)
    )
    if qry.first() is not None:
        qry.update({'otp_code': otp_code, 'created_date': dt.datetime.now()})
    else:
        db.add(twofa)
    db.commit()

    # send sms, disabled this feature since twilio only works with verfied numbers
    # print(send_otp(otp_code, to_number))

    return {"status_code": 200, "message": f"OTP is {otp_code}, sms not sent as number is not verfied on twilio server"}


def verify_twofa(user_id, otp_code, db):

    user = db.query(models.TwoFA).get(user_id)

    if int(user.otp_code) == otp_code and (dt.datetime.now() - user.created_date) <= dt.timedelta(seconds=60):
        return {"status_code": "200", "message": "verfied"}
    else:
        return {"status_code": "400", "message": "Invalid or expired code"}


def send_otp(otp_code, to_number="+6581633116"):
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
