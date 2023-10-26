from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("settings/", include("settings.urls")),
    path('admin/hamon-diag/', admin.site.urls),
    path('',include("product.urls")),
    path("auth/",include("authentication.urls")),
    path("blog/",include("blog.urls")),
]
if settings.DEBUG :
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )