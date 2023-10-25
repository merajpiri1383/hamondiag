from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from settings.forms import ProductForm,CategoryForm,TagFrom
from product.models import Product,Category,Tag
from django.views.generic import CreateView,UpdateView,DeleteView,FormView,View
class BaseView(LoginRequiredMixin) :
    template_name = "settings/product.html"
    success_url = reverse_lazy("settings:settings")
class CreateProduct(BaseView,CreateView):
    form_class = ProductForm
class CreateCategoryView(BaseView,CreateView):
    form_class = CategoryForm
class CreateTag(BaseView,CreateView):
    form_class = TagFrom
class SettingsView(View):
    def get(self,request):
        return render(request,"settings/settings.html")