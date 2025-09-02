from django.urls import path
from .views import create_product_view, seller_dashboard, delete_product, home_view, ProductDetailView, ProductsListView, MyProductsView, MyProductsDetailView, product_detailed_view, seller_profile_view


app_name = 'products'
urlpatterns = [

    # --------- API Endpoints ---------
    path('api/products/', ProductsListView.as_view(), name="products"),
    # List all products (with search & filter)

    path('api/product/detail/<int:pk>/', ProductDetailView.as_view(), name='api_product_detail' ),
    # View details of a single product (by primary key)

    path('api/seller/products/', MyProductsView.as_view(), name="seller_products"),
    # List & create products belonging to logged-in seller

    path('api/seller/product/detail/<int:pk>/', MyProductsDetailView.as_view(), name='seller_product_detail'),
    # View, update, or delete a seller’s specific product

    # --------- Template Views ---------
    path('seller_profile/<int:seller_id>', seller_profile_view, name='seller_profile'),
    # Public page showing seller profile and their products

    path('product_detail/<int:product_id>/', product_detailed_view, name='product_detail'),
    # Public page showing details of one product

    path('product_create/', create_product_view, name='product_create'),
    # Form for sellers to create a product

    path('seller_dashboard/', seller_dashboard, name='seller_dashboard'),
    # Dashboard where seller can see their products

    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    # Delete a product (only if owned by seller)

    path('home/', home_view, name='home' ),
    # Homepage with all products and categories

    path('', home_view, name='home'),
    # Default route → homepage


]