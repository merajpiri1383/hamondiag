from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse_lazy
class Category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(unique=True)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(blank=True,unique=True,null=True)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(Tag,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    price = models.IntegerField(null=True,blank=True)
    is_exist = models.BooleanField(default=True)
    image = models.ImageField(upload_to="media")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(validators=[
        MinValueValidator(0),MaxValueValidator(100)
    ],null=True,blank=True)
    category = models.ManyToManyField(to=Category,blank=True,related_name="products")
    tags = models.ManyToManyField(to=Tag,blank=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse_lazy("product:product-detail",args=[self.id])
class Image(models.Model):
    image = models.ImageField(upload_to="media")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")