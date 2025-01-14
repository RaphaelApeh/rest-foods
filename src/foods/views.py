from django.shortcuts import render

from rest_framework.views import APIView

from .models import Category

def home_page_view(request):
    category = Category.objects.select_related("food").all()
    context = {"object_list": category}
    return render(request, "foods/items.html", context)