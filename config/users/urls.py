from django.urls import path
from .views import about_us_view, register, login_view, logout_view, profile_view, register_seller, update_profile, UserListView, SellerListView, UserDetailView, UserRegisterView, UserLoginView, UserLogoutView, SellerDetailView, SellerRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Namespace for this app's URLs
app_name = 'users'

urlpatterns = [
    # ---------- API Endpoints ----------

    # Endpoint for obtaining a new access and refresh token pair (user logs in here)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint for refreshing the access token using a valid refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Get list of all users (API)
    path('api/users/details/', UserListView.as_view(), name="users_details" ),

    # Get details of a single logged-in user (API)
    path('api/user/profile/', UserDetailView.as_view(), name="user_profile"  ),

    # Register a new user via API
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),


    # Login user via API
    path('api/user/login/', UserLoginView.as_view(), name='login'),

    # Logout user via API
    path('api/user/logout/', UserLogoutView.as_view(), name='logout'),

    # Seller_registration API
    path('api/seller/register/', SellerRegisterView.as_view(), name='seller_register'),

    # Get list of all sellers (API)
    path('api/sellers/details/', SellerListView.as_view(), name="seller_details"),

    # Get seller profile details (API)
    path('api/seller/profile/', SellerDetailView.as_view(), name='seller_profile'),





    # ---------- Template Views ----------

    # About Us page
    path('about_us/', about_us_view, name='about_us'), 

    # Register page (HTML form)
    path('register/', register, name='register'),

    # Login page (HTML form)
    path('login/', login_view, name='login'),

    # Logout (redirects user after logout)
    path('logout/', logout_view, name="logout"),

    # Profile page for logged-in user
    path('profile/', profile_view, name="profile"),

    # Seller registration page
    path('seller_registration/', register_seller, name='register_seller'),

    # Update user profile page
    path('profile_update', update_profile, name='profile_update' )

    
]