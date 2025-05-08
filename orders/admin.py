from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Cart_item)
class CartItem_Admin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity')
    search_fields = ('user__username', 'item__name')

@admin.register(models.Order)
class Order_Admin(admin.ModelAdmin):
    list_display = ('user', 'total', 'orderTime')
    list_filter = ('status', 'order_method', 'payment_method')
    def total(self, obj): return obj.subtotal + obj.charge

@admin.register(models.Order_item)
class OrderItem_Admin(admin.ModelAdmin):
    list_display = ('order', 'item_name', 'item_price', 'quantity')