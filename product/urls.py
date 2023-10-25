from django.urls import path
from product import views
app_name= "product"
urlpatterns = [
    path("",views.MainView.as_view(),name="main"),
    path("<slug:slug>/",views.ProductDetailView.as_view(),name="product-detail"),
]