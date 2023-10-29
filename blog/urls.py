from django.urls import path
from blog import views
urlpatterns = [
    path("",views.BlogListView.as_view(),name="blogs"),
    path("add-blog/",views.BlogView.as_view(),name="add-blog"),
    path("edit-blog/<slug:slug>/",views.BlogContent.as_view(),name="edit-blog"),
    path("delete-content/<slug:slug>/<int:id>/<str:model>",views.DeleteContentView.as_view(),name="delete-content"),
    path("<slug:slug>/",views.BlogDetailView.as_view(),name="blog"),
    path("detail/<slug:slug>/",views.BlogDetailView.as_view(),name="blog-detail"),
    path("delete/<slug:slug>/",views.BlogDeleteView.as_view(),name="blog-delete"),
]