from asgiref.sync import async_to_sync

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

from channels.layers import get_channel_layer

from .consumers import NOTIFICATION

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def get_food_qs(self):
        return self.food_set.all()
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    short_description = models.CharField(max_length=15)
    image = models.ImageField(upload_to="images", default="default.jpg")
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

    @property
    def get_category_name(self):
        return self.category.name
    
    @property
    def get_order_qs(self):
        return self.order_set.all()

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    note = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.note[:5]}...."



def send_users_food_notification(sender, instance, created, **kwargs):

    if created:
        channel_layer = get_channel_layer()
        event = {
            "type":"send_notification",
            "message": f"A food as been add {instance.name}"
        }
        async_to_sync(channel_layer.group_send)(NOTIFICATION, event)


post_save.connect(send_users_food_notification, User)