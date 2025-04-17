from django.shortcuts import render
from .models import FoodItem, Category

def homepage(request):
    categories = Category.objects.all()
    food_items = FoodItem.objects.filter(available=True)
    return render(request, 'menu/homepage.html', {
        'categories': categories,
        'food_items': food_items
    })
