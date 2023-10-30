from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from authentication.manager import UserManager
from django.contrib.auth import get_user_model
from iranian_cities.fields import OstanField,ShahrField
from iranian_cities.models import Ostan
class User(AbstractBaseUser,PermissionsMixin):
    mobile = models.CharField(max_length=11,unique=True)
    otp = models.SlugField(blank=True,null=True)
    otp_created = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    backend = "authentication.backend.AuthBackend"
    objects = UserManager()
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.mobile
posts_method = [
    ("noramal","عادی"),
    ("fast","پیشتاز")
]
class PostInfo(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name="post")
    name = models.CharField(max_length=250)
    mobile = models.PositiveIntegerField()
    mobile_2 = models.PositiveIntegerField()
    state = OstanField()
    city = ShahrField()
    code_post = models.PositiveIntegerField()
    address = models.TextField()
    post_method = models.CharField(max_length=15,choices=posts_method,default="noramal")
    is_ok = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} {self.mobile}"