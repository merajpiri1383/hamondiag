from django.template import Library
from product.models import Product
from jalali_date.templatetags.jalali_tags import to_jalali
register = Library()
@register.filter(name="name_cut")
def product_name(value):
    if len(value) < 20 :
        return value
    return f"{value[0:20]}..."
@register.filter(name="discount_price")
def discount_price(product:Product):
    price = None
    if product.discount :
        price = product.price * (100 - product.discount) / 100
        return str(price)[0:-2]
    return product.price
@register.filter(name="name_title")
def product_title(value):
    if len(value) < 10 :
        return value
    return f"{value[0:10]}..."
@register.filter(name="product_total")
def product_total(pack):
    count = pack.count
    price = pack.product.price
    if pack.product.discount :
        price = (100 - pack.product.discount) /100 * price
        return str(count * price)[0:-2]
    return count * price
@register.filter(name="date")
def product_total(time):
    return to_jalali(time,strftime='%H:%M:%S | %Y/%m/%d ')