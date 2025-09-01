from django.db import models
from users.models import SellerProfile
# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ProductListings(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    location = models.CharField(max_length=100)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
