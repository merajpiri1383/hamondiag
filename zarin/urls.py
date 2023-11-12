from django.urls import path
from zarin import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('request/', login_required(views.request_payment), name='request'),
    path('verify/', login_required(views.verify), name='verify'),
]