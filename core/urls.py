from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path("zarin/",include("zarin.urls")),
    path("blog/",include("blog.urls")),
    path("auth/",include("authentication.urls")),
    path("settings/", include("settings.urls")),
    path('admin/hamon-diag/', admin.site.urls),
    path('',include("product.urls")),
]
if settings.DEBUG :
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )