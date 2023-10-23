from django.template import Library
from product.models import Product
register = Library()
@register.filter(name="name_cut")
def product_name(value):
    if len(value) < 20 :
        return value
    return f"{value[0:20]}..."
@register.filter(name="discount_price")
def discount_price(product:Product):
    price = None
    if product.discount > 0 :
        price = product.price * (100 - product.discount) / 100
        return price
    return product.price