from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, primary_key=True)
    category_slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__ (self):
        return self.category_name
    
class MenuItem(models.Model):
    item_name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(blank=True)
    item_image = models.ImageField(upload_to="menu")
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    item_slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="Uncategorized")

class Review(models.Model):
    item = models.ForeignKey(MenuItem, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], blank=False)
    image = models.ImageField(blank=True, null=True, upload_to='review_images/')
    is_featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')