from django import forms
from .models import UserDetail, SellerProfile
from django.contrib.auth.forms import UserCreationForm


class UserDetailForm(UserCreationForm):

   
    class Meta:
        model = UserDetail
        fields = ['username', 'email', 'password1', 'password2']
      

class UserUpdateForm(forms.ModelForm):

   
    class Meta:
        model = UserDetail
        fields = ['username','image', 'full_name', 'location']
      
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label="password")

class SellerProfileForm(forms.ModelForm):

    
    class Meta:

        model = SellerProfile
        fields = ['phone_number', 'id_number', 'shop_name', 'location']