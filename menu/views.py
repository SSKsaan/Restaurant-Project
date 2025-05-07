from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import MenuItem, Category

# Create your views here.
class MenuList(ListView):
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['Category'] = self.category
        return context
    
    def get_queryset(self):
        queryset = MenuItem.objects.all()
        self.category = None
        slug = self.kwargs.get('slug')
        if slug:
            self.category = get_object_or_404(Category, category_slug=slug)
            queryset = queryset.filter(category=self.category)
        return queryset
    
class ItemDetails(DetailView):
    model = MenuItem
    template_name = 'menu_item.html'
    context_object_name = 'item'
    slug_url_kwarg = 'item_slug'