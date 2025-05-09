from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.views import redirect_to_login
from .models import MenuItem, Category, Review
from .forms import ReviewForm

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
