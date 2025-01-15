from rest_framework import generics


from ..models import Food, Order, Category
from ..serializers import FoodSerializer, CategorySerializer


class FoodListView(generics.ListAPIView):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer


food_list_view = FoodListView.as_view()