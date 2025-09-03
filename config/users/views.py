from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserDetailForm, LoginForm,  SellerProfileForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserDetail, SellerProfile
from rest_framework import generics, permissions, response, status
from .serializers import UserDetailSerializer, SellerDetailSerializer, UserRegisterSerializer, SellerRegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.http import JsonResponse
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.views import APIView


# -------------------- API Views --------------------

# API endpoint for user registration
class UserRegisterView(generics.CreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserRegisterSerializer


# API endpoint for user login (using Django sessions)
class UserLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user against DB
        user = authenticate(request, username=username, password=password)

        if user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            # Return Tokkens in response
            return Response({
                'refresh': str(refresh),
                'access' : str(refresh.access_token)

            }, status=status.HTTP_200_OK)
                
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)


# API endpoint for user logout
class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "refresh_token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logout successful"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except TokenError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# API endpoint to list all users (admin only)
class UserListView(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]

# API endpoint to retrieve/update/delete the logged-in user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Only allow users to access their own info

        return self.request.user

# API endpoint to register a seller (requires login)
class SellerRegisterView(generics.CreateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

# API endpoint to list all sellers (admin only)
class SellerListView(generics.ListAPIView):
    # Only allow users to access their info
    queryset = SellerProfile.objects.all()
    serializer_class = SellerDetailSerializer
    permission_classes = [permissions.IsAdminUser]

# API endpoint to allow sellers  retrieve/update/delete their details 
class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.seller_profile



# -------------------- Template Views (Frontend Pages) --------------------

# "About Us" page
def about_us_view(request):
    
    return render(request, 'users/about_us.html')


# User registration form (HTML)
def register(request):
    """
    Handles user registration
    If request is POST register user
    Elif request is GET display registration form
    """
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            user = form.save() # save user to database
            login(request, user)            
            return redirect('products:home') # Redirect user to a homepage
        
        else:
            messages.error(request, 'Please Correct the errors below')
    else:
        form = UserDetailForm() # For empty GET request display blank registration form
    
    return render(request, 'users/signup.html', {'form': form})

# User login form (HTML)
def login_view(request):
    """
    Handles User login request
    If request is POST proceed to check the system
    If request is GET  display loginform    
    """
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                # Retrieve the username from the cleaned form data
                username = form.cleaned_data.get('username')
                #Retrieve password from cleaned data
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password) # check for details with the database and ensure that a user data is present before loggin in
                if user is not None:
                    login(request, user) # logs in the user
                    return redirect('products:home') # Directs them to homepage logged where they can interact with goods
                else:
                    messages.error(request, 'Please enter valid username or password')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form':form})


@login_required # Ensures that for a user to logout they must have logged in prior
def logout_view(request):
    """
    Logs out user and redirects to homepage.
    """
    logout(request)
    return redirect('products:home') # Take the users back to landing page after signing out

# User profile page (HTML)
@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


# Seller registration (HTML)
@login_required
def register_seller(request):
    """
    Handles seller registration (profile creation).
    Prevents users from registering twice.
    """
    if hasattr(request.user, "seller_profile" ):
        return redirect('users:seller_dashboard')
    
    if request.method == 'POST':
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            return redirect('users:seller_dashboard')
    else:
        form = SellerProfileForm()
    
    return render(request, 'users/register_seller.html', {'form':form} )


@login_required
def update_profile(request):

    """
    Allow logged-in users to update their profiles
    """
    
    if request.method =='POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form':form})
