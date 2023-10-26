from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from blog.models import Blog,Text,Picture
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from blog.forms import BlogForm,PicturContentForm,TextContentForm
class BlogView(View):
    def get(self,request):
        form = BlogForm()
        blogs = Blog.objects.all().order_by("-created")
        return render(request,"blog/add-blog.html",{"form":form,"blogs":blogs})
    def post(self,request):
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,"blog/add-blog.html",{"form":form})
class BlogContent(View):
    blog = None
    last_blogs =None
    def get(self,request,slug):
        try :
            self.blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            pass
        self.last_blogs = Blog.objects.all().order_by("-created")[0:5]
        form1 = TextContentForm()
        print(self.blog.)
        form2 = PicturContentForm()
        return render(request,"blog/edit-blog.html",{"textform":form1,"pictureform":form2
                      ,"blog":self.blog,"last_blogs":self.last_blogs})
    def post(self,request,slug):
        form1 = TextContentForm(data=request.POST)
        form2 = PicturContentForm(request.POST,request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.blog_id = Blog.objects.get(slug=slug).id
            obj.save()
            return redirect("edit-blog",slug)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.blog_id = Blog.objects.get(slug=slug).id
            obj.save()
            return redirect("edit-blog", slug)
        return render(request,"blog/edit-blog.html",{"textform":form1,"pictureform":form2
                      ,"blog":self.blog,"last_blogs":self.last_blogs})