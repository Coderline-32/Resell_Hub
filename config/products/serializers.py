from rest_framework import serializers
from .models import Category, ProductListings

# Serializer for product categories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] # only return category name


# Serializer for all products (general use)
class ProductsSerializer(serializers.ModelSerializer):
     # Get category name from related Category model
    category_name = serializers.CharField(source="category.name", default=None)

    class Meta:
        model = ProductListings
        fields = ['id', 'title', 'description', 'price', 'image', 'location', 'category_name', 'seller', 'created_at' ]

        # These fields cannot be changed directly via API
        read_only_fields = ['id', 'seller', 'created_at']

# Serializer for seller’s own products (no seller field exposed)
class MyProductsSerializer(serializers.ModelSerializer):
    # SlugRElated allows for display user category name on get methods and accepts write
    category = serializers.PrimaryKeyRelatedField (queryset=Category.objects.all())
        

    class Meta:
        model = ProductListings
        fields = ['id', 'title', 'description', 'price', 'image', 'location', 'category', 'created_at', ]
        read_only_fields = ['id', 'created_at']

    
    