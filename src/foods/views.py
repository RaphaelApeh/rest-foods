from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category

def home_page_view(request):

    return HttpResponse("<h1>Home Page</h1>")

def detail_view(request, name: str):
    qs = Category.objects.all()[:5]
    category = get_object_or_404(Category, name__icontains=name)
    context = {"object": category, 'object_list': qs}

    return render(request, "foods/items.html", context)