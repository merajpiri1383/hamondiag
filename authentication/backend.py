from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
class AuthBackend(ModelBackend):
    def authenticate(self,request,mobile,otp,**kwargs):
        try :
            user = get_user_model().objects.get(mobile=mobile)
            print(otp)
            if int(user.otp) == otp :
                print("true")
                user.is_active = True
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