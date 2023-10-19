from django.dispatch import receiver
from django.db.models.signals import post_save
from time import sleep
from random import randint
from django.contrib.auth import get_user_model
@receiver(signal=post_save,sender=get_user_model())
def create_otp(sender,instance,created,**kwargs):
    user = get_user_model().objects.get(mobile=instance.mobile)
    user.otp = randint(1000,9999)
    user.save()
    sleep(120)
    if not user.is_active :
        user.delete()