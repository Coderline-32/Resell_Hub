from django import forms
from .models import UserDetail, SellerProfile
from django.contrib.auth.forms import UserCreationForm


# ------------------ User Registration Form ------------------
# Extends Django's built-in UserCreationForm to register new users
class UserDetailForm(UserCreationForm):

   
    class Meta:
        model = UserDetail
        fields = ['username', 'email', 'password1', 'password2']
        # password1 & password2 are handled by UserCreationForm (with validation)
      

# ------------------ User Update Form ------------------
# Allows users to update their profile info
class UserUpdateForm(forms.ModelForm):

   
    class Meta:
        model = UserDetail
        fields = ['username','image', 'full_name', 'location']

# ------------------ Login Form ------------------
# Basic login form (not using Django’s built-in AuthenticationForm)   
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label="password")
     # PasswordInput widget hides characters when typing


# ------------------ Seller Profile Form ------------------
# For users who want to register/update as sellers
class SellerProfileForm(forms.ModelForm):

    
    class Meta:

        model = SellerProfile
        fields = ['phone_number', 'id_number', 'shop_name', 'location']
        # extra details specific to sellers