from django.db import models
class Settings(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
class Mobiles(models.Model):
    setting = models.ForeignKey(Settings,on_delete=models.CASCADE,related_name="phones")
    phone = models.PositiveIntegerField()