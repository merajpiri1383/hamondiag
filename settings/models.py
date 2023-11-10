from django.db import models
from django.utils.text import slugify
class Settings(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.TextField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    phone = models.PositiveIntegerField()
    def __str__(self):
        return self.name
class Poster(models.Model):
    setting = models.ForeignKey(to=Settings,on_delete=models.CASCADE,
                                related_name="posters")
    img = models.ImageField(upload_to="posters", null=True, blank=True)