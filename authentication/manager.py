from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self,mobile,password,**extra_kwargs):
        if not mobile :
            raise ValueError("mobile is required !!!")
        user = self.model(mobile=mobile,**extra_kwargs)
        user.set_password(password)
        user.save()
    def create_superuser(self,mobile,password,**extra_kwargs):
        extra_kwargs.setdefault("is_active",True)
        extra_kwargs.setdefault("is_staff",True)
        extra_kwargs.setdefault("is_superuser",True)
        if not extra_kwargs.get("is_active") :
            raise ValueError("is_active must be True !!!")
        if not extra_kwargs.get("is_staff") :
            raise ValueError("is_active must be True !!!")
        if not extra_kwargs.get("is_superuser") :
            raise ValueError("is_superuser must be True !!!")
        return self.create_user(mobile,password,**extra_kwargs)