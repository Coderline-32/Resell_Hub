from rest_framework import serializers
from .models import UserDetail, SellerProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed




User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'date_joined', 'full_name', 'location', 'image']
        read_only_fields = ['id', 'email', 'date_joined']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            return serializers.ValidationError("'password': Passwords do not match")
        return attrs
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    


class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = SellerProfile
        fields = ['shop_name', 'phone_number', 'id_number', 'location' ]

class SellerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
              
        model = SellerProfile
        fields = ['id', 'shop_name', 'phone_number', 'id_number', 'location' ]
        read_only_fields = ['id']

