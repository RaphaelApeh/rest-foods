from channels.generic.websocket import AsyncJsonWebsocketConsumer


NOTIFICATION = "notification"

class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        
        
        self.notification_name = NOTIFICATION

        await self.channel_layer.group_add(self.notification_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        
        await self.channel_layer.group_discard(self.notification_name, self.channel_name)
        print("Disconnect with", code)

    async def send_notification(self, event):
        
        await self.send_json(event["message"])