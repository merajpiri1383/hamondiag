from django import forms
from blog.models import Blog,Picture,Text
class BlogForm(forms.ModelForm):
    class Meta :
        model = Blog
        fields = ["name","picture"] 
class PicturContentForm(forms.ModelForm):
    class Meta :
        model = Picture
        fields = ["content"]
    labels = {
        "content": "تصویر"
    }
class TextContentForm(forms.ModelForm):
    class Meta :
        model = Text
        fields = ["content","color","font_size"]
    labels = {
        "content" : "متن",
        "color": "رنگ",
        "font_size":"انداره"
    }