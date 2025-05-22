from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.Cart_view, name='cart'),
    path('checkout/', views.Checkout_view, name='checkout'),
    path('details/<int:pk>', views.Order_Details, name='order_details'),
    path('update/', views.update_quantity, name='update_quantity'),
]