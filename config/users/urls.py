from django.urls import path
from .views import index_view, home_view, register, login_view, logout_view, profile_view, register_seller, seller_dashboard

urlpatterns = [
    path('', index_view, name='index'), 
    path('home/', home_view, name='home' ),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
    path('seller_registration/', register_seller, name='register_seller'),
    path('seller_dashboard/', seller_dashboard, name='seller_dashboard'),
]