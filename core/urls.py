from django.contrib import admin
from django.urls import path,include
from core.views import MainView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MainView.as_view(),name="main"),
    path("auth/",include("authentication.urls")),
    path("__drbug__/",include("debug_toolbar.urls")),
]
if settings.DEBUG :
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )