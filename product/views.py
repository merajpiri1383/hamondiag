from django.shortcuts import render
from django.views.generic.base import View
from product.models import Product,Category
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
        }
        return render(request,"product/main.html",context)
class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product