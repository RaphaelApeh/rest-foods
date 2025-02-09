from rest_framework import generics
from django_filters import rest_framework as filters

from ..filters import FoodFilterSet, RestaurantFilterSet
from ..models import Food, Restaurant
from ..pagination import RestPageNumberPagination
from ..serializers import FoodSerializer, RestaurantSerializer


class FoodListView(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_class = FoodFilterSet


food_list_view = FoodListView.as_view()

class FoodDetailView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'pk'

food_detail_view = FoodDetailView.as_view()


class RestaurantListView(generics.ListAPIView):
    pagination_class = RestPageNumberPagination
    queryset = Restaurant.objects.select_related("user")
    serializer_class = RestaurantSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = RestaurantFilterSet