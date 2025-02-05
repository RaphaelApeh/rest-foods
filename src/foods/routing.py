from django.urls import path

from .consumers import NotificationConsumer
from messaging.consumers import MessageWebsocketConsumer

websocket_urlpatterns = [
    path("notification/", NotificationConsumer.as_asgi()),

    path("messages/<str:pk>/", MessageWebsocketConsumer.as_asgi())
]