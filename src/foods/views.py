from django.views.generic import ListView
from .models import Food


class FoodListView(ListView):
    model = Food
    queryset = Food.objects.select_related("category")
    template_name = "foods/food_list.html"
    paginate_by = 2

food_list_view = FoodListView.as_view()