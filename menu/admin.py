from django.contrib import admin
from . import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',)}
admin.site.register(models.Category, CategoryAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'item_slug': ('item_name',)}
    list_display = ['item_name', 'price', 'category', 'is_available', 'is_featured']
    list_editable = ['is_available', 'is_featured']
    search_fields = ['item_name']
admin.site.register(models.MenuItem, MenuItemAdmin)