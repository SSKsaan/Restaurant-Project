from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',)}

@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'item_slug': ('item_name',)}
    list_display = ['item_name', 'price', 'category', 'is_available', 'is_featured']
    list_editable = ['is_available', 'is_featured']
    search_fields = ['item_name']

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['get_user_username', 'get_item_name', 'rating']
    search_fields = ['content',]

    def get_user_username(self, obj):
        return obj.user.username

    def get_item_name(self, obj):
        return obj.item.item_name

    get_user_username.short_description = 'User'
    get_item_name.short_description = 'Item'