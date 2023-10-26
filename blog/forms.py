from django import forms
from blog.models import Blog,Picture,Text
class BlogForm(forms.ModelForm):
    class Meta :
        model = Blog
        fields = ["name","picture"] 
class PicturContentForm(forms.ModelForm):
    class Meta :
        model = Picture
        fields = ["img"]
    labels = {
        "img": "تصویر"
    }
class TextContentForm(forms.ModelForm):
    class Meta :
        model = Text
        fields = ["text","color","font_size"]
    labels = {
        "text" : "متن",
        "color": "رنگ",
        "font_size":"انداره"
    }