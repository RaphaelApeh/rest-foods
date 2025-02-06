from django.contrib import admin

from .models import Category, Food, Restaurant


class FoodInline(admin.StackedInline):
    model = Food
    extra = 0

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [FoodInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    ...