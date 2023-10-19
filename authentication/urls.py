from django.urls import path
from authentication import views
app_label = "authentication"
urlpatterns = [
    path("login/",views.AuthView.as_view(),name="login")
]