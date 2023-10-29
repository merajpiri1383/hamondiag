from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
class AuthBackend(ModelBackend):
    def authenticate(self,request,mobile,otp,**kwargs):
        try :
            user = get_user_model().objects.get(mobile=mobile)
            if int(user.otp) == otp :
                user.is_active = True
                print("user in here")
                user.save()
                return user
            return None
        except get_user_model().DoesNotExist :
            return None
    def get_user(self,user_id):
        try :
            return get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist :
             return None