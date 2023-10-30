from django.urls import path
from authentication import views
from django.contrib.auth.decorators import login_required
app_label = "authentication"
urlpatterns = [
    path("login/",views.AuthView.as_view(),name="login"),
    path("verify/<str:phone>/",views.VerifyView.as_view(),name="verify"),
    path("profile/",login_required(views.ProfileView.as_view()),name="profile"),
    path("logout/",login_required(views.logout_view),name="logout"),
    path("post-info/",login_required(views.PostInfoView.as_view()),name="post-info"),
    path("last-carts/",login_required(views.LastCartsView.as_view()),name="last-carts"),
]