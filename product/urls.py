from django.urls import path
from product import views
from django.contrib.auth.decorators import login_required
app_name= "product"
urlpatterns = [
    path("cart/",login_required(views.CartView.as_view()),name="cart"),
    path("",views.MainView.as_view(),name="main"),
    path("<slug:slug>/",views.ProductDetailView.as_view(),name="product-detail"),
] 