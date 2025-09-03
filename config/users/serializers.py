from rest_framework import serializers
from .models import UserDetail, SellerProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed




User = get_user_model()  # dynamically fetch the User model (custom or default)


# ------------------ User Serializers ------------------

# Serializer for viewing user details (profile, etc.)
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'date_joined', 'full_name', 'location', 'image']
        read_only_fields = ['id', 'email', 'date_joined']


# Serializer for registering new users
class UserRegisterSerializer(serializers.ModelSerializer):
    # password fields (write_only means they won’t be exposed in API responses)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'}) # uses Django’s password validatio
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    # Custom validation to ensure both passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            return serializers.ValidationError("'password': Passwords do not match")
        return attrs
    
     # Create new user (Django's create_user handles password hashing)
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    

# ------------------ Seller Serializers ------------------

# Serializer for viewing seller details
class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = SellerProfile
        fields = ['shop_name', 'phone_number', 'id_number', 'location' ]


# Serializer for registering seller profiles
class SellerRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
              
        model = SellerProfile
        fields = ['shop_name', 'id_number', 'phone_number', 'location' ]
    

    
        

