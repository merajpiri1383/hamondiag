from django import forms
from product.models import Product,Category,Tag
from settings.models import Settings
class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = ["name","price","discount","image","category","tags","description"]
class CategoryForm(forms.ModelForm):
    class Meta :
        model = Category
        fields = ["name"]
class TagFrom(forms.ModelForm):
    class Meta :
        model = Tag
        fields = ["name"]
class SettingsForm(forms.ModelForm):
    class Meta :
        model = Settings
        fields = ["name","poster","phone","email","address","about"]
        labels = {
            "name":"نام",
            "poster":"پوستر",
            "phone" : "شماره",
            "address":"آدرس",
            "email":"ایمیل",
            "about":"درباره"
        }