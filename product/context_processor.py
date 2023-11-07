from blog.models import Blog
def last_blogs(request):
    blogs = Blog.objects.all().order_by("-created")[0:5]
    return {"last_blogs" : blogs}