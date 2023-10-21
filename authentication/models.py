from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from authentication.manager import UserManager
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