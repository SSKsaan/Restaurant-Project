from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

# Create your models here.
class Cart_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.quantity * self.item.price
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    charge = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_method = models.CharField(
        max_length=20,
        choices=[('delivery', 'Delivery'), ('pickup', 'Pickup')],
        default='delivery'
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[('cash', 'Cash'), ('digital', 'Bkash')],
        default='cash'
    )
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending'
    ) 
    contact = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    orderTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class Order_item(models.Model):
    order = models.ForeignKey(Order, related_name='ordered_items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=99)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.item_price * self.quantity