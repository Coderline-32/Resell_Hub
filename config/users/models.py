from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


# Custom user model extending Django's built-in AbstractUser
class UserDetail(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)    
    email = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)

# Seller profile model linked to UserDetail
class SellerProfile(models.Model):
    
    # One-to-one relationship ensures each user has at most one seller profile
    user = models.OneToOneField(UserDetail, on_delete=models.CASCADE, related_name='seller_profile')
    shop_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=True)

    # Seller’s ID for verification purposes (must be unique and min 7 chars)
    id_number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(7)],
        unique=True
        )
    location = models.CharField(max_length=50)
    
