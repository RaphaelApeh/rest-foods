from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer

from foods.consumers import NOTIFICATION

User = get_user_model()

def send_user_created_notification(instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        event = {
            "type":"send_notification",
            "message": f"A user as joined on {instance.date_joined:%c}"
        }
        async_to_sync(channel_layer.group_send)(NOTIFICATION, event)

post_save.connect(send_user_created_notification, sender=User)
