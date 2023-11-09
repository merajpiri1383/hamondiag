from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.urls import reverse_lazy
from product.models import Product,Category,Cart,CartProduct
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.messages import warning
from django.views.generic.detail import DetailView
class MainView(View):
    def get(self,request):
        page = request.GET.get("p",1) 
        category = request.GET.get("c")
        discount = request.GET.get("d")
        products = Product.objects.all().order_by("-created")
        discounts = Product.objects.filter(discount__gt=0)
        if category :
            try :
                x = Category.objects.get(slug=category)
                products = Product.objects.filter(category=x)
            except :
                pass
        if discount:
            products = Product.objects.filter(discount__gt=0)
        paginator = Paginator(products,per_page=20)
        try :
            products = paginator.page(page)
        except EmptyPage:
            products= paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            products = paginator.page(1)
        context = {
            "products" : products,
            "categorys" : Category.objects.all(),
            "most_sells" : Product.objects.all().order_by("count_buy")[0:6]
        }
        return render(request,"product/main.html",context)
class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.object.tags.all()
        similar_products = []
        for tag in tags :
            products = Product.objects.filter(tags__slug=tag.slug).exclude(
                slug = self.object.slug
            )[0:3]
            for product in products:
                if not product in similar_products :
                    similar_products.append(product)
        context["similar_products"] = similar_products
        return context
class CartView(View):
    def get(self,request):
        cart = None
        try :
            cart = request.user.carts.get(is_paid=False)
        except :
            pass
        dis = False
        total = 0
        for cart_product in cart.cart_products.all() :
            price = cart_product.product.price
            if cart_product.product.discount :
                dis = True
                price = (100-cart_product.product.discount) * price / 100
            total += price * cart_product.count
        if dis :
            total = str(total)[0:-2]
        return render(request,"product/cart.html",{"cart":cart,"total":total})
class AddProductView(View):
    def get(self,request,slug,mode):
        product = None
        cart = None
        cart_product = None
        try :
            product = Product.objects.get(slug=slug)
            if not product.price :
                warning(request,f"جهت خرید '{product.name}' تماس بگیرید")
                return redirect("product:main")
        except :
            return redirect("product:main")
        try :
            cart = request.user.carts.get(is_open=True,is_paid=False)
        except :
            cart = Cart.objects.create(user=request.user)
        try :
            cart_product = cart.cart_products.get(product=product)
        except :
            cart_product = CartProduct.objects.create(product=product,cart=cart)
        if mode == "add" :
            cart_product.count += 1
            cart_product.save()
        if mode == "remove" :
            if cart_product.count == 1 :
                cart_product.delete()
            else :
                cart_product.count -= 1
                cart_product.save()
        return redirect("product:cart")
class CompleteCart(View):
    def get(self,request):
        cart = request.user.carts.filter(is_open=True,is_paid=False).first()
        try :
            postinfo = request.user.post
        except :
            warning(request,"شما هنوز اطاعات پستی را کامل نکرده اید .")
            return redirect("post-info")
        dis = False
        total = 0
        for cart_product in cart.cart_products.all():
            price = cart_product.product.price
            if cart_product.product.discount:
                dis = True
                price = (100 - cart_product.product.discount) * price / 100
            total += price * cart_product.count
        if dis:
            total = str(total)[0:-2]
        return render( request , "product/ultimate.html",{
            "cart":cart,
            "total" : total,
            "postinfo": postinfo
        })
class DeleteProduct(View):
    def get(self,request,slug):
        if request.user.is_staff :
            try:
                obj = Product.objects.get(slug=slug)
                obj.delete()
            except:
                warning(request, "محصولی با این نام وجود ندارد")
        return redirect("product:main")