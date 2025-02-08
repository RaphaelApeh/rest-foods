from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime

from rest_framework import serializers

from .models import Category, Food, Restaurant

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', "get_full_name",  'email', "date_joined"]

    def get_date_joined(self, obj):
        return naturaltime(obj.date_joined)

class FoodSerializer(serializers.ModelSerializer):

    restaurant = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Food
        fields = ['name', "restaurant", "category", 'short_description', 'price', 'image', 'quantity']

    def get_restaurant(self, obj):
        return obj.restaurant.name


class RestaurantSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    food = FoodSerializer(many=True, read_only=True, source="restaurants")
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["name", "user", "description", "food", "address", "image", "timestamp"]

    def get_timestamp(self, obj):
        return naturalday(obj.timestamp)