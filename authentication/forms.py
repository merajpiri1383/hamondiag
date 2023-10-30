from django.contrib.auth import get_user_model
from django import forms
from authentication.models import PostInfo
class AuthForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["mobile"]
        widgets = {
            "mobile" : forms.TextInput(attrs={
                "placeholder": "شماره موبایل",
            })
        }
    def clean(self):
        mobile = self.cleaned_data.get("mobile")
        if len(str(mobile)) <11:
            self.add_error("mobile","شماره معتبر نمی باشد")
        if not str(mobile).startswith("09"):
            self.add_error("mobile","شماره معتبر نمی باشد")
class VerifyForm(forms.Form):
    verify_code = forms.IntegerField(widget=forms.TextInput(attrs={
        "placeholder": "کد تایید",
    }))
    def clean(self):
        code = str(self.cleaned_data.get("verify_code"))
        if len(code) > 4 and len(code) < 4 :
            self.add_error("verify_code","کد نامعتبر می باشد ")
class PostInfoForm(forms.ModelForm):
    class Meta :
        model = PostInfo
        fields = ["name","mobile","mobile_2","code_post","state","city","address"]
        labels = {
            "name" :"نام و نام خانوادگی",
            "mobile":"شماره",
            "mobile_2":"شماره اضطراری",
            "code_post":"کد پستی",
            "state":"استان",
            "city" :"شهر",
            "address":"ادرس",
        }