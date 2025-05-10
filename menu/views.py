from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import MenuItem, Category, Review
from .forms import ReviewForm
from orders.models import Cart_item

# Create your views here.
def MenuList(request, slug=None):
    if slug:
       category = get_object_or_404(Category, category_slug=slug)
       items = MenuItem.objects.filter(category=category)
    else:
       category = None
       items = MenuItem.objects.all()
    categories = Category.objects.all()
    return render(request, 'menu_list.html', 
                  {'items': items, 'categories': categories, 'category': category})
    
def ItemDetails(request, item_slug):
    item = get_object_or_404(MenuItem, item_slug=item_slug)
    check_review = Review.objects.filter(item=item, user=request.user).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect_to_login(request.path)
        form = ReviewForm(request.POST, request.FILES, instance=check_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.item = item
            review.save()
            return redirect('item', item_slug=item_slug)
    else:
        form = ReviewForm(instance=check_review)
        
    reviews = item.reviews.select_related('user').order_by('-created_at')

    return render(request, 'item_detail.html', {'item': item, 'form': form, 'reviews': reviews})

@login_required
def Add_to_Cart(request, item_slug):
    item = get_object_or_404(MenuItem, item_slug=item_slug)
    cart_item, created = Cart_item.objects.get_or_create(user=request.user, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'message': f'{item.item_name} added to your cart!'})