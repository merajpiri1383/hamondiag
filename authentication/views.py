from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import get_user_model
from authentication import forms
class AuthView(View):
    def get(self,request):
        form = forms.AuthForm()
        print("jj")
        return render(request, "authentication/auth.html", {"form":form})
    def post(self,request):
        form = forms.AuthForm(data=request.POST)
        if form.is_valid():
            mobile = form.cleaned_data.get("mobile")
        return render(request, "authentication/auth.html",{"form":form})