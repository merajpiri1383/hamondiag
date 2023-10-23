from django.shortcuts import render
from django.views.generic.base import View
from product.models import Product,Image
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
class MainView(View):
    def get(self,request):
        page = request.GET.get("p",1)
        products = None
        paginator = Paginator(Product.objects.all(),per_page=3)
        try :
            products = paginator.page(page)
        except EmptyPage:
            pass
        except PageNotAnInteger:
            products = paginator.page(paginator.orphans)
        context = {
            "products" : products
        }
        return render(request,"product/main.html",context)