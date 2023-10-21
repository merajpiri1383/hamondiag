from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
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
            if get_user_model().objects.filter(mobile=mobile):
                user = get_user_model().objects.get(mobile=mobile)
                user.otp = randint(1000,9999)
                user.save()
                print(user.otp)
                otp.send_otp(user)
            else :
                print("user not exist")
                user = form.save(commit=False)
                user.otp = randint(1000, 9999)
                user.set_password("hamon_diag")
                otp.send_otp(user)
                print(user.otp)
                user.save()
            return redirect("verify",mobile)
        return render(request, "authentication/auth.html",{"form":form})
class VerifyView(View):
    def get(self,request,phone):
        form = forms.VerifyForm()
        print(phone)
        return render(request,"authentication/verify.html",{"form":form})
    def post(self,request,phone):
        form = forms.VerifyForm(data=request.POST)
        if form.is_valid():
            try :
                user = get_user_model().objects.get(mobile=phone)
                x = authenticate(request, mobile=phone, otp=
                form.cleaned_data.get("verify_code"))
                if x:
                    login(request,x)
                    # redirect to products
                else :
                    form.add_error("verify_code", "کد تایید نامعتبر می باشد ")
            except :
                form.add_error("verify_code","کد تایید نامعتبر می باشد ")
        return render(request,"authentication/verify.html",{"form":form})