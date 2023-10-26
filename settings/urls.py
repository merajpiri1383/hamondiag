from django.urls import path
from settings import views
app_name="settings"
urlpatterns = [
    path("",views.SettingsView.as_view(),name="settings"),
    #   product
    path("add-product/",views.CreateProduct.as_view(),name="add-product"),
    path("update-product/<slug:slug>/",views.UpdateProduct.as_view(),name="product-update"),
    #   category
    path("add-category/",views.CreateCategoryView.as_view(),name="add-category"),
    path("delete-category/<slug:slug>/",views.DeleteCategory.as_view(),name="category-delete"),
    #   tag
    path("add-tag/",views.CreateTag.as_view(),name="add-tag"),
    path("delete-tag/<slug:slug>/",views.DeleteTag.as_view(),name="delete-tag")
]