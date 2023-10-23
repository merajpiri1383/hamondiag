from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator
class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True,blank=True,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media")
    discount = models.IntegerField(validators=[
        MinValueValidator(0),MaxValueValidator(100)
    ],default=0)
    description = models.TextField()
    tag = TaggableManager()
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args,**kwargs)
class Image(models.Model):
    image = models.ImageField(upload_to="media")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,
                                related_name="images")