from django.urls import path
from settings import views
from django.contrib.auth.decorators import login_required
app_name="settings"
urlpatterns = [
    path("",login_required(views.SettingsView.as_view()),name="settings"),
    #   product
    path("add-product/",login_required(views.CreateProduct.as_view()),name="add-product"),
    path("update-product/<slug:slug>/",login_required(views.UpdateProduct.as_view()),name="product-update"),
    #   category
    path("add-category/",login_required(views.CreateCategoryView.as_view()),name="add-category"),
    path("delete-category/<slug:slug>/",login_required(views.DeleteCategory.as_view()),name="category-delete"),
    #   tag
    path("add-tag/",login_required(views.CreateTag.as_view()),name="add-tag"),
    path("delete-tag/<slug:slug>/",login_required(views.DeleteTag.as_view()),name="delete-tag"),
    #   total
    path("total/",login_required(views.Total.as_view()),name="total"),
    path("delete-poster/<int:id>/",login_required(views.DeletePoster.as_view()),name="delete-poster")
]