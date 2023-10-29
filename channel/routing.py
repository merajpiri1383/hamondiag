from django.urls import path
from channel.consumer import WSConsumer
websocket_urlpatterns = [
    path("ws/cart/",WSConsumer.as_asgi())
]