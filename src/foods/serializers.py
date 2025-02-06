from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Category, Food, Restaurant

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'get_full_name', 'email']


class FoodSerializer(serializers.ModelSerializer):

    restaurant = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['name', "restaurant", 'short_description', 'price', 'image', 'quantity']

    def get_restaurant(self, obj):
        return obj.restaurant.name

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['name']


class RestaurantSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    food = FoodSerializer(many=True, read_only=True, source="restaurants")

    class Meta:
        model = Restaurant
        fields = ["name", "user", "description", "food", "address", "image"]

    def get_user(self, obj):
        return obj.user.username