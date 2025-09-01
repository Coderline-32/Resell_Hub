from rest_framework import serializers
from .models import Category, ProductListings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", default=None)

    class Meta:
        model = ProductListings
        fields = ['id', 'title', 'description', 'price', 'image', 'location', 'category_name', 'seller', 'created_at' ]
        read_only_fields = ['id', 'seller', 'created_at']

class MyProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", default=None)

    class Meta:
        model = ProductListings
        fields = ['id', 'title', 'description', 'price', 'image', 'location', 'category_name',  'created_at' ]
        read_only_fields = ['id', 'created_at']