from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    short_description = models.CharField(max_length=15)
    #image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    note = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.note[:5]}...."