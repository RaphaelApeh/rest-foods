from asgiref.sync import async_to_sync

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer

from foods.consumers import NOTIFICATION

User = get_user_model()

class EmailVerification(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


def send_user_created_notification(instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        event = {
            "type":"send_notification",
            "message": f"A user as joined on {instance.date_joined:%c}"
        }
        async_to_sync(channel_layer.group_send)(NOTIFICATION, event)

post_save.connect(send_user_created_notification, sender=User)
