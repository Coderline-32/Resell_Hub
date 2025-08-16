from django import forms
from .models import UserDetail
from django.contrib.auth.forms import UserCreationForm


class UserDetailForm(UserCreationForm):

    class Meta:
        model = UserDetail
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']
        help_texts = {field: '' for field in fields}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label="password")