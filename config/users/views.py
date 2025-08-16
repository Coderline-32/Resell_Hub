from django.shortcuts import render, redirect
from .forms import UserDetailForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index_view(request):
    return render(request, 'users/index.html')

@login_required(login_url = 'index') #Ensures only logged inusers can access the page
def home_view(request):
    return render(request,  'users/home.html')

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
            return redirect('home') # Redirect user to a homepage
        
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
                    return redirect('home') # Directs them to homepage logged where they can interact with goods
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
    return redirect('index') # Take the users back to landing page after signing out
