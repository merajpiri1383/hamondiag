from django.contrib.auth import get_user_model
from django import forms
class AuthForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["mobile"]
        labels = {"mobile": "شماره موبایل"}
        widgets = {
            "mobile" : forms.TextInput(attrs={
                "type":"number"
            })
        }
    def clean(self):
        mobile = self.cleaned_data.get("mobile")
        if len(str(mobile)) <11:
            self.add_error("mobile","شماره معتبر نمی باشد")
        if not str(mobile).startswith("09"):
            self.add_error("mobile","شماره معتبر نمی باشد")