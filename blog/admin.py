from django.contrib import admin
from blog.models import Blog,Picture,Text,Content
admin.site.register(Blog)
admin.site.register(Text)
admin.site.register(Picture)
admin.site.register(Content)