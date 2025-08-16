from django.urls import path
from .views import index_view, home_view, register, login_view, logout_view

urlpatterns = [
    path('', index_view, name='index'), 
    path('home/', home_view, name='home' ),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout")
]