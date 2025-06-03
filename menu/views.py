from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.http import JsonResponse
from .models import MenuItem, Category, Review
from .forms import ReviewForm
from orders.models import Cart_item

# Create your views here.
def MenuList(request, category_slug=None):
    if category_slug:
       category = get_object_or_404(Category, category_slug=category_slug)
       items = MenuItem.objects.filter(category=category).order_by('item_name')
    else:
       category = None
       items = MenuItem.objects.all().order_by('item_name')
    categories = Category.objects.all()
    return render(request, 'menu_list.html', 
                  {'items': items, 'categories': categories, 'category': category})
    
def ItemDetails(request, item_slug):
    item = get_object_or_404(MenuItem, item_slug=item_slug)
    recommendations = MenuItem.objects.filter(is_available=True).exclude(item_name=item.item_name).order_by('?')[:6]
    
    check_review = Review.objects.filter(item=item, user=request.user).first() if request.user.is_authenticated else None
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to submit a review.')
            return redirect_to_login(request.path)
        form = ReviewForm(request.POST, request.FILES, instance=check_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.item = item
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('item', item_slug=item_slug)
        else:
            messages.error(request, 'Review submission failed! Please try again.')
    else:
        form = ReviewForm(instance=check_review)
        
    reviews = item.reviews.select_related('user').order_by('-timestamp')

    return render(request, 'item_details.html', {
        'item': item, 
        'form': form, 
        'reviews': reviews,
        'recommendations': recommendations
        }
    )

def Add_to_Cart(request, item_slug):
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'Please log in to add items in your cart.'})
        
    item = get_object_or_404(MenuItem, item_slug=item_slug)
    cart_item, created = Cart_item.objects.get_or_create(user=request.user, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'message': f'{item.item_name} added to your cart!'})