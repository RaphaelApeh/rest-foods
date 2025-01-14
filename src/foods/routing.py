from django.urls import path

from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path("notification/", NotificationConsumer.as_asgi()),
]