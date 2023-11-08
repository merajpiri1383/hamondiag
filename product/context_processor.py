from blog.models import Blog
def last_blogs(request):
    blogs = Blog.objects.all().order_by("-created")[0:5]
    return {"last_blogs" : blogs}
def total_products(request):
    cart = request.user.carts.filter(is_open=True,is_paid=False).first()
    total = 0
    for cart_product in cart.cart_products.all() :
        total += cart_product.count
    return {"total_products":total}