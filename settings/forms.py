from django import forms
from product.models import Product,Category,Tag,Image
from settings.models import Settings,Poster
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
        fields = ["name","phone","email","address","about"]
        labels = {
            "name":"نام",
            "phone" : "شماره",
            "address":"آدرس",
            "email":"ایمیل",
            "about":"درباره"
        }
class PosterForm(forms.ModelForm):
    class Meta :
        model = Poster
        fields = ["img"]
class ImageForm(forms.ModelForm):
    is_save = forms.BooleanField()
    class Meta :
        model = Image
        fields = ["image","is_save"]