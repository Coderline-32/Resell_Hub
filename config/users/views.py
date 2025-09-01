from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserDetailForm, LoginForm,  SellerProfileForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserDetail, SellerProfile
from rest_framework import generics, permissions, response, status
from .serializers import UserDetailSerializer, SellerDetailSerializer, UserRegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views import View


# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return JsonResponse({"message": "Login successful"}, status=200)
                
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)


class UserLogoutView(View) :
    def post(self, request):
        logout(request) 
        return JsonResponse({"message": "Logout successful"}, status=200)



class UserListView(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Only allow users to access their info

        return self.request.user

class SellerListView(generics.ListAPIView):
    # Only allow users to access their info
    queryset = SellerProfile.objects.all()
    serializer_class = SellerDetailSerializer
    permission_classes = [permissions.IsAdminUser]









def index_view(request):
    
    return render(request, 'users/index.html')



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
    Function which provides a way for users to logout after signing in
    """
    logout(request)
    return redirect('users:index') # Take the users back to landing page after signing out

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def register_seller(request):
    """
    Handle seller registration 
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
    Allow users to update their profiles
    """
    
    if request.method =='POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form':form})
