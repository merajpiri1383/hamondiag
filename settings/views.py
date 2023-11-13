from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models import Settings,Poster
from django.contrib.messages import warning
from authentication.models import PostInfo
from django.urls import reverse_lazy
from settings.forms import (ProductForm,CategoryForm,TagFrom,
                            SettingsForm,PosterForm,ImageForm)
from product.models import Product,Category,Tag,Image,Cart
from django.views.generic import CreateView,UpdateView,DeleteView,FormView,View
from django.views.generic.base import TemplateResponseMixin
class BaseView(LoginRequiredMixin) :
    template_name = "settings/product.html"
    success_url = reverse_lazy("settings:settings")
class CreateProduct(BaseView,CreateView):
    form_class = ProductForm
class CreateCategoryView(BaseView,CreateView):
    form_class = CategoryForm
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = Category.objects.all() 
        context["url"] = "settings:category-delete"
        return context
class CreateTag(BaseView,CreateView):
    form_class = TagFrom
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = Tag.objects.all()
        context["url"] = "settings:delete-tag" 
        return context
class SettingsView(View):
    def get(self,request):
        return render(request,"settings/settings.html")
class UpdateProduct(TemplateResponseMixin,View):
    template_name = "settings/product.html"
    product = None
    def dispatch(self,request,slug):
        try :
            self.product = Product.objects.get(slug=slug)
        except :
            return redirect("settings:settings")
        return super().dispatch(request,slug)
    def get(self,request,slug):
        form = ProductForm(instance=self.product)
        add_image_form = ImageForm()
        return self.render_to_response({
            "form" : form,
            "add_image_form" : add_image_form,
            "product" : self.product
        })
    def post(self,request,slug):
        form = ProductForm(request.POST,request.FILES,instance=self.product)
        add_image_form = ImageForm(request.POST,request.FILES)
        print(add_image_form.is_valid())
        print(form.is_valid())
        if form.is_valid() and not add_image_form.is_valid():
            print("form 1")
            form.save()
            return redirect("settings:product-update",self.product.slug)
        if add_image_form.is_valid() :
            obj = add_image_form.save(commit=False)
            obj.product = self.product
            if self.product.images.all().count() <= 3 :
                obj.save()
            else :
                warning(request,"شما ۴ تصویر برای این محصول دارید ")
            return redirect("settings:product-update",self.product.slug)
class DeleteImgsProduct(View):
    def get(self,request,pk):
        try :
            obj = Image.objects.get(id=pk)
            obj.delete()
            return redirect("product:main")
        except :
            return redirect("product:main")
class DeleteCategory(DeleteView):
    template_name = "product/main.html"
    model = Category
    success_url = reverse_lazy("product:main")
class DeleteTag(DeleteView):
    template_name = "product/main.html"
    model = Tag
    success_url = reverse_lazy("settings:settings")
class Total(View):
    def get(self,request):
        if request.user.is_staff:
            setting = Settings.objects.all().first()
            form = SettingsForm(instance=setting)
            form_img = PosterForm()
            imgs = Poster.objects.all()
            return render(request,"settings/total.html",{"form":form,"form_img":form_img,"imgs":imgs})
    def post(self,request,slug=None):
        if request.user.is_staff:
            setting = Settings.objects.all().first()
            form = SettingsForm(request.POST,instance=setting)
            form_img = PosterForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("settings:settings")
            if form_img.is_valid():
                obj = form_img.save(commit=False)
                try :
                    obj.setting = Settings.objects.all().first()
                    obj.save()
                except :
                    warning(request,"جهت افزودن پوستر ابتدا باید تنظمات کلی را پر کنید")
                    return redirect("settings:total")
                return redirect("settings:settings")
            return render(request,"settings/total.html",{"form":form,"form_img":form_img})
class DeletePoster(View):
    def get(self,request,id):
        try :
            poster = Poster.objects.get(id=id)
            poster.delete()
        except :
            warnings(request,'پوستری با این id وجود ندارد')
        return redirect("settings:settings")
def completed_carts(request):
    carts = Cart.objects.filter(is_open=False,is_paid=True)
    objects = []
    for cart in carts :
        objects.append({
            "cart": cart,
            "postinfo" : PostInfo.objects.get(user=cart.user)
        })
    return render(request,"settings/carts.html",{"object":objects})