from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User  # Correctly import User
from .forms import SignUpForm, LoginForm  # Ensure these forms exist if used

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)  # Use User
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  # Redirect to login page after signup
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def home(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    return render(request, 'home.html', {'username': username})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to login page after logout