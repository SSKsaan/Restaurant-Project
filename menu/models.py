from django.db import models

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
