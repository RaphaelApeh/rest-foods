from django.views import generic
from django.contrib.auth import mixins

from .forms import RestaurantForm
from .models import Food, Restaurant


class FoodListView(generic.ListView):
    model = Food
    queryset = Food.objects.select_related("category")
    template_name = "foods/food_list.html"
    paginate_by = 2

food_list_view = FoodListView.as_view()


class RestaurantCrateView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = "foods/restaurant-form.html"
    model = Restaurant
    success_url = "/"
    form_class = RestaurantForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


restaurant_create_view = RestaurantCrateView.as_view()