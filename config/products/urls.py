from django.urls import path
from .views import create_product_view, seller_dashboard, delete_product, home_view, ProductsCreateView, ProductDetailView, ProductsListView


app_name = 'products'
urlpatterns = [
    path('api/products/', ProductsListView.as_view(), name="products"),
    path('api/product/create/', ProductsCreateView.as_view(), name='product_create' ),
    path('api/detail/<int:pk>/', ProductDetailView.as_view(), name='update' ),





    path('product_create/', create_product_view, name='product_create'),
    path('seller_dashboard/', seller_dashboard, name='seller_dashboard'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('home/', home_view, name='home' )

]