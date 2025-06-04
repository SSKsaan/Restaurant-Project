from . import forms
from .models import Cart_item, Order, Order_item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse

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
    user = request.user
    items = Cart_item.objects.filter(user=user)

    if request.method == 'POST':
        if 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            cart_item = get_object_or_404(Cart_item, id=item_id, user=user)
            messages.success(request, f"Item '{cart_item.item.item_name}' removed from cart.")
            cart_item.delete()
            return redirect('cart')

        elif 'clear_cart' in request.POST:
            items.delete()
            messages.success(request, "All items cleared from your cart.")
            return redirect('cart')

        elif 'checkout' in request.POST:
            order_method = request.POST.get('order_method')
            return redirect('checkout', order_method=order_method)
        
    return render(request, 'cart.html', {'Cart_items': items})

@login_required
def update_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        if item_id and quantity and quantity.isdigit():
            cart_item = Cart_item.objects.filter(id=item_id, user=request.user).first()
            if cart_item:
                quantity = max(1, int(quantity))
                cart_item.quantity = quantity
                cart_item.save()
                return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@login_required
def Checkout_view(request):
    order_method = request.POST.get('order_method')
    if request.method == 'GET' and not order_method:
        messages.error(request, 'No order method specified.')
        return redirect('cart')
    request.session['order_method'] = order_method
    
    Items = Cart_item.objects.filter(user=request.user)
    Subtotal = sum(item.subtotal for item in Items)
    DeliveryCharge = 100.0 if order_method=='delivery' else 0
    Total = Subtotal + DeliveryCharge

    FormClass = forms.DeliveryForm if order_method=='delivery' else forms.PickupForm
    if request.method == 'POST' and 'ordered' in request.POST:
        form = FormClass(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.subtotal = Subtotal
            order.charge = DeliveryCharge
            order.order_method = order_method
            order.payment_method = request.POST.get('payment_method')
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
            messages.success(request, 'Order placed successfully! Please check your Email.')
            return redirect('home')
        else:
            messages.error(request, 'Order placement failed! Please try again.')
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
def Order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'order_details.html', {'order': order})
