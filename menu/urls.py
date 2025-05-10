from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList, name='menu'),
    path('item/<slug:item_slug>', views.ItemDetails, name='item'),
    path('category/<slug:category_slug>', views.MenuList, name='filtered_category'),
    path('add_to_cart/<slug:item_slug>', views.Add_to_Cart, name='add_to_cart'),
]