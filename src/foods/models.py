from asgiref.sync import async_to_sync

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings

from channels.layers import get_channel_layer

from .consumers import NOTIFICATION

User = settings.AUTH_USER_MODEL


class Restaurant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to="restaurant")
    foods = models.ManyToManyField("Food", blank=True, related_name="foods")
    timestamp = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email} {self.name}"
    

class Category(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name="restaurants", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    short_description = models.CharField(max_length=15)
    image = models.ImageField(upload_to="images", default="default.jpg")
    price = models.FloatField(default=99.9)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name



def send_users_food_notification(sender, instance, created, **kwargs):

    if created:
        channel_layer = get_channel_layer()
        event = {
            "type":"send_notification",
            "message": f"A food as been add {instance.name}"
        }
        async_to_sync(channel_layer.group_send)(NOTIFICATION, event)


post_save.connect(send_users_food_notification, sender=Food)