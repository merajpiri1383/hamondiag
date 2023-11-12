from django.urls import path
from product import views
from django.contrib.auth.decorators import login_required
app_name= "product"
urlpatterns = [
    # product
    path("complete-cart/",login_required(views.CompleteCart.as_view()),name="complete-cart"),
    path("cart/",login_required(views.CartView.as_view()),name="cart"),
    path("",views.MainView.as_view(),name="main"),
    path("<slug:slug>/",views.ProductDetailView.as_view(),name="product-detail"),
    path("delete-product/<slug:slug>/",login_required(views.DeleteProduct.as_view()),name="delete-product"),
    path("product/<slug:slug>/<mode>/",login_required(views.AddProductView.as_view()),name="product"),
] 