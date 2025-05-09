from . import forms
from .models import Cart_item, Order, Order_item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_email(request, order):
    subject = "Order Confirmation"
    from_mail = settings.EMAIL_HOST_USER
    to_mail = request.user.email

    html_content = render_to_string('mail.html', {'user': request.user, 'order': order})
    plain_content = strip_tags(html_content)
    mail = EmailMultiAlternatives(subject, plain_content, from_mail, [to_mail])
    mail.attach_alternative(html_content, "text/html")
    mail.send()


# Create your views here.
@login_required
def Cart_view(request):
    items = Cart_item.objects.filter(user=request.user)
    subtotal = sum(item.subtotal for item in items)
    if request.method == 'POST':
        order_method = request.POST.get('order_method')
        return redirect('checkout', order_method=order_method)
    return render(request, 'cart.html', {'Cart_items': items, 'Subtotal': subtotal})


@login_required
def Checkout_view(request, order_method):
    Items = Cart_item.objects.filter(user=request.user)
    Subtotal = sum(item.subtotal for item in Items)
    DeliveryCharge = 100 if order_method=='delivery' else 0
    Total = Subtotal + DeliveryCharge
    
    FormClass = forms.DeliveryForm if order_method=='delivery' else forms.PickupForm
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            user = request.user
            subtotal = Subtotal
            charge = DeliveryCharge
            order_method = order_method
            order.save()

            for item in Items:
                Order_item.objects.create(
                    order = order,
                    item_name = item.item.item_name,
                    item_price = item.item.price,
                    quantity = item.quantity
                )
            Items.delete()
            send_email(request, order)
    else:
        form = FormClass()

    return render(request, 'checkout.html', 
                  {
                      'form': form,
                      'items': Items,
                      'subtotal': Subtotal,
                      'charge': DeliveryCharge,
                      'total': Total,
                      'order_method': order_method
                  }
    )
        

@login_required
def Order_Details(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'order_details.html', {'order': order})
