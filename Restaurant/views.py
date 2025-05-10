from django.shortcuts import render
from menu.models import MenuItem, Review

def HomeView(request):
    items = MenuItem.objects.filter(is_featured=True)
    reviews = Review.objects.filter(is_featured=True).select_related('user')
    return render(request, 'home.html', {'items': items, 'reviews': reviews})