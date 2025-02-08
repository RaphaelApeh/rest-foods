import django_filters

from .models import Food, Category, Restaurant


class CategoryFilterSet(django_filters.FilterSet):
    
    class Meta:
        model = Category
        fields = ['name']


class FoodFilterSet(django_filters.FilterSet):

    class Meta:
        model = Food
        fields = ['name', 'short_description', 'quantity']


class RestaurantFilterSet(django_filters.FilterSet):

    class Meta:
        model = Restaurant 
        fields = ["user__username", "address"]