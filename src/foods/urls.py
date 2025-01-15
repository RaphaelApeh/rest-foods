from django.urls import path

from . import views

app_name = "foods"

urlpatterns = [
    path("", views.home_page_view, name="home"),

    path("<str:name>/", views.detail_view, name="detail-page")
]