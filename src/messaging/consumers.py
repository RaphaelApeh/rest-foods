from django.contrib.auth import get_user_model

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

User  = get_user_model()


class MessageWebsocketConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
        
        await self.accept()

    async def disconnect(self, code):
            print(f"Disconnect {code}")