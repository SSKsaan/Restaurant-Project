from django import forms
from .models import Order

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['contact', 'address', 'note', 'payment_method']
        widgets = {
            'address': forms.Textarea(attrs={'required': True}),
        }

class PickupForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['contact', 'note', 'payment_method']