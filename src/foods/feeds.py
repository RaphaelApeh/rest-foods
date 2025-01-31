from django.contrib.syndication.views import Feed

from .models import Food

class FoodFeed(Feed):
    title = "Food"
    link = "/rss/"
    description = "Update on the lastest Food"

    def items(self):
        return Food.objects.order_by("-timestamp")[:2]
    
    def item_title(self, item):
        return item.name
    
    def item_description(self, item):
        return item.short_description
    
    def item_link(self, item):
        return "/"