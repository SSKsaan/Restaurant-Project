from django import forms
from .models import Order

class DeliveryForm(forms.ModelForm):
    address = forms.CharField(required=True)
    class Meta:
        model = Order
        fields = ['payment_method', 'address', 'note']

class PickupForm(forms.ModelForm):
    class Meta:
        model = Order
        Fields = ['payment_method', 'note']