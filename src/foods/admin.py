from django.contrib import admin

from .models import Category, Food, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


class OrderStackedInline(admin.StackedInline):
    model = Order
    extra = 0

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [OrderStackedInline]