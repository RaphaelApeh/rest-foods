from django.urls import path

from .consumer import NotificationConsumer

websocket_urlpatterns = [
    path("notification/", NotificationConsumer.as_asgi())
]