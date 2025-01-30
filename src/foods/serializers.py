from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Category, Food, Order

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'get_full_name', 'email']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['note']


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['name', 'short_description', 'price', 'image', 'quantity']


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['name']