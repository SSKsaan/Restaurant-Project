from django.urls import path
from .views import MenuList, ItemDetails

urlpatterns = [
    path('', MenuList.as_view(), name='menu'),
    path('item/<slug:item_slug>', ItemDetails.as_view(), name='item'),
    path('category/<slug:category_slug>', MenuList.as_view(), name='filtered_category'),
]