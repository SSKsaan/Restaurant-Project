from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.Cart_view, name='cart'),
    path('checkout/', views.Checkout_view, name='checkout'),
    path('update/', views.update_quantity, name='update_quantity'),
    path('detail/<int:pk>', views.Order_detail, name='order_detail'),
]