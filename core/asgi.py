import os

import django
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channel.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
            websocket_urlpatterns
        )
    ),
  )
})