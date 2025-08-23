from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class UserDetail(AbstractUser):
    phone_number = models.CharField(max_length=15)

class SellerProfile(models.Model):
    user = models.OneToOneField(UserDetail, on_delete=models.CASCADE, related_name='seller_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    id_number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(7)],
        unique=True
        )
    location = models.CharField(max_length=50)
    
