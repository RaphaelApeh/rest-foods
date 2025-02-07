from django.urls import path

from . import views

urlpatterns = [
    path("restaurants/", views.RestaurantListView.as_view()),
    path("foods/", views.food_list_view),
    path("foods/<int:pk>/", views.food_detail_view)
]