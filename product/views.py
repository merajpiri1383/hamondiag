from django.shortcuts import render,redirect
from django.views.generic.base import View
from product.models import Product,Category,Cart,CartProduct
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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
        return render(request,"product/cart.html",{"cart":cart})