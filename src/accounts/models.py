from asgiref.sync import async_to_sync

from django.db import models
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer

from foods.consumers import NOTIFICATION

User = get_user_model()

class EmailVerification(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6, blank=True, null=True, editable=False, db_index=True, unique=True)
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
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
        
        _email = EmailVerification.objects.create(user=instance, verification_code=get_random_string(5))
        instance.email_user("Comfirm Email to Continue", f"verification code:\n {_email.verification_code}")

post_save.connect(send_user_created_notification, sender=User)
