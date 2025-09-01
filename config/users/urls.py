from django.urls import path
from .views import index_view, register, login_view, logout_view, profile_view, register_seller, update_profile, UserListView, SellerListView, UserDetailView, UserRegisterView, UserLoginView, UserLogoutView, SellerDetailview

app_name = 'users'

urlpatterns = [
    path('details/', UserListView.as_view(), name="users_details" ),
    path('user/info/', UserDetailView.as_view(), name="user_profile"  ),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('sellers/details/', SellerListView.as_view(), name="seller_details"),
    path('seller/profile', SellerDetailview.as_view(), name='seller_profile'),



    path('', index_view, name='index'), 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
    path('seller_registration/', register_seller, name='register_seller'),
    path('profile_update', update_profile, name='profile_update' )
    
]