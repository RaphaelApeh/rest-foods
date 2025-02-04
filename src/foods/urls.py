from django.urls import path

from . import views

app_name = "foods"

urlpatterns = [

    path("", views.food_list_view),
    path("new/", views.restaurant_create_view, name="rest-create")

]