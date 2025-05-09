from django.urls import path
from .views import MenuList, ItemDetails

urlpatterns = [
    path('', MenuList, name='menu'),
    path('item/<slug:item_slug>', ItemDetails, name='item'),
    path('category/<slug:category_slug>', MenuList, name='filtered_category'),
]