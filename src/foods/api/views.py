from rest_framework import generics
from django_filters import rest_framework as filters

from ..filters import FoodFilterSet
from ..models import Food
from ..serializers import FoodSerializer

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