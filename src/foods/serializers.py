from django.contrib.auth import get_user_model

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
    
        return obj.date_joined.strftime("%Y-%m-%d")

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
        return obj.timestamp.strftime("%Y-%m-%d")
    
    def create(self, validated_data):
        request = self.context.get("request")
        assert request is not None
        assert request.user.is_authenticated is True

        user = validated_data.pop("user")
        
        return Restaurant.objects.create(user=user, **validated_data)
    

    def update(self, instance, validated_data):
        
        for name, value in validated_data.items():
            assert name in self.fields
            setattr(instance, name, value)
            instance.save()

        return instance