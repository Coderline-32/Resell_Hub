from rest_framework import serializers
from .models import Category, ProductListings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListings
        fields = '__all__'
