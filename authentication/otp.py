import datetime
from django.contrib.auth import get_user_model
from threading import Thread
from time import sleep
from random import randint
def is_otp_expired(user):
    now = datetime.datetime.now(datetime.timezone.utc)
    otp_time = user.otp_created
    if (now-otp_time).seconds > 120 :
        return True
    return False
def send_otp_thread(user):
    # send otp to user
    sleep(10)
    if user.is_active :
        user.otp = None
        user.save()
    else :
        user.delete()
def send_otp(user):
    task = Thread(target=send_otp_thread,args=[user])
    task.start()