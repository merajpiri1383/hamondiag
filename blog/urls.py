from django.urls import path
from blog import views
urlpatterns = [
    path("add-blog/",views.BlogView.as_view(),name="add-blog"),
    path("edit-blog/<slug:slug>/",views.BlogContent.as_view(),name="edit-blog"),
] 