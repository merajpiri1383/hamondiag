from django import forms
from product.models import Product,Category,Tag
class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = ["name","price","discount","image","category","tags"]
class CategoryForm(forms.ModelForm):
    class Meta :
        model = Category
        fields = ["name"]
class TagFrom(forms.ModelForm):
    class Meta :
        model = Tag
        fields = ["name"]