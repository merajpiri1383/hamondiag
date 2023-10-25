from django.urls import path
from settings import views
app_name="settings"
urlpatterns = [
    path("",views.SettingsView.as_view(),name="settings"),
    #   product
    path("add-product/",views.CreateProduct.as_view(),name="add-product"),
    #   category
    path("add-category/",views.CreateCategoryView.as_view(),name="add-category"),
    #   tag
    path("add-tag/",views.CreateTag.as_view(),name="add-tag"),
]