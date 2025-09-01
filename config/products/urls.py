from django.urls import path
from .views import create_product_view, seller_dashboard, delete_product, home_view, ProductDetailView, ProductsListView, MyProductsView, MyProductsDetailView


app_name = 'products'
urlpatterns = [
    path('api/products/', ProductsListView.as_view(), name="products"),
    path('api/product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail' ),
    path('api/seller/products/', MyProductsView.as_view(), name="seller_products"),
    path('api/seller/product/detail/<int:pk>/', MyProductsDetailView.as_view(), name='seller_product_detail'),


    path('product_create/', create_product_view, name='product_create'),
    path('seller_dashboard/', seller_dashboard, name='seller_dashboard'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('home/', home_view, name='home' )

]