from django.contrib import admin
from product.models import Product,Image,Tag,Category
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Image)