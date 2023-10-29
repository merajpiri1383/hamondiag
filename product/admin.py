from django.contrib import admin
from product.models import Product,Image,Tag,Category,Cart,CartProduct
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(CartProduct)