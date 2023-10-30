from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import View,TemplateResponseMixin
from django.contrib.auth import get_user_model,login,authenticate,logout
from authentication import otp
from authentication import forms
from random import randint
class AuthView(View):
    def get(self,request):
        form = forms.AuthForm()
        return render(request, "authentication/auth.html", {"form":form})
    def post(self,request):
        form = forms.AuthForm(data=request.POST)
        if form.is_valid():
            mobile = form.cleaned_data.get("mobile")
            user , created = get_user_model().objects.get_or_create(mobile=mobile)
            otp_code = randint(1000,9999)
            user.otp = otp_code
            user.save()
            otp.send_otp(user=user)
            print(otp_code)
            return redirect("verify",mobile)
        return render(request, "authentication/auth.html",{"form":form})
class VerifyView(View):
    def get(self,request,phone):
        form = forms.VerifyForm()
        return render(request,"authentication/verify.html",{"form":form})
    def post(self,request,phone):
        form = forms.VerifyForm(data=request.POST)
        if form.is_valid():
            try :
                x = authenticate(request, mobile=phone, otp=
                form.cleaned_data.get("verify_code"))
                if x:
                    login(request,x)
                    return redirect("product:main")
                else :
                    form.add_error("verify_code", "کد تایید نامعتبر می باشد ")
            except :
                form.add_error("verify_code","کد تایید نامعتبر می باشد ")
        return render(request,"authentication/verify.html",{"form":form})
class ProfileView(View):
    def get(self,request):
        return render(request,"authentication/profile.html")
def logout_view(request):
    logout(request)
    return redirect("product:main")
class PostInfoView(TemplateResponseMixin,View):
    template_name = "authentication/post_info.html"
    postinfo = None
    def dispatch(self,request):
        self.postinfo = request.user.post
        return super().dispatch(request)
    def get(self,request):
        form = forms.PostInfoForm(instance=self.postinfo)
        return self.render_to_response({
            "form" : form
        })
    def post(self,request):
        form = forms.PostInfoForm(data=request.POST,instance=self.postinfo)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.is_ok = True
            obj.save()
            return redirect("product:cart")
        return self.render_to_response({
            "form":form
        })
class LastCartsView(View):
    def get(self,request):
        carts = request.user.carts.all().filter(is_paid=True,is_open=False)
        return render(request,"authentication/last_carts.html",{"carts":carts})