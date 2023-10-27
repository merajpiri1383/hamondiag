from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Blog(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    picture = models.ImageField(upload_to="pictures")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.name
text_font_choice = [
    ("h1" , "heading 1"),
    ("h2" , "heading 2"),
    ("h3" , "heading 3"),
    ("h4" , "heading 4"),
    ("h5" , "heading 5"),
    ("h6" , "heading 6"),
]
text_colors = [
    ("danger","red"),
    ("primary","blue"),
    ("secondary","gray"),
    ("info","light blue"),
    ("dark","black"),
    ("warning","yellow"),
]
class Content(models.Model):
    blog = models.ForeignKey(to=Blog,on_delete=models.CASCADE,related_name="contents")
    content_type = models.ForeignKey(to=ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type","object_id")
class BaseContent(models.Model):
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name="childs")
    created = models.DateTimeField(auto_now_add=True)
    class Meta :
        abstract = True
class Text(models.Model):
    content = models.TextField(null=True,blank=True)
    color = models.CharField(max_length=15,choices=text_colors,default="dark")
    font_size = models.CharField(max_length=15,choices=text_font_choice,default="h6")
class Picture(models.Model):
    content = models.ImageField(upload_to="pictures",null=True,blank=True)