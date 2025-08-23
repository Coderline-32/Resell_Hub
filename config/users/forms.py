from django import forms
from .models import UserDetail, SellerProfile
from django.contrib.auth.forms import UserCreationForm


class UserDetailForm(UserCreationForm):

   
    class Meta:
        model = UserDetail
        fields = ['username', 'email', 'password1', 'password2']
      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label="password")

class SellerProfileForm(forms.ModelForm):

    
    class Meta:

        model = SellerProfile
        fields = ['first_name', 'last_name', 'phone_number', 'id_number', 'shop_name', 'location']