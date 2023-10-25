from django.shortcuts import render
from django.views.generic.base import View
from product.models import Product,Image
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.detail import DetailView
class MainView(View):
    def get(self,request):
        page = request.GET.get("p",1)
        products = None
        paginator = Paginator(Product.objects.all().order_by("-created")
                              ,per_page=20)
        try :
            products = paginator.page(page)
        except EmptyPage:
            products= paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            products = paginator.page(1)
        context = {
            "products" : products
        }
        return render(request,"product/main.html",context)
class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product