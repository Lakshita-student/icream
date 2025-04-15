from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout 
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def Product(request):
    return render(request,'home/Product.html')

def signup_view(request):
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            first_name=first,
            last_name=last,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')
    return render(request, 'home/signup_login.html')  # Replace with actual template

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace with your homepage
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'home/signup_login.html')  # Same template

def logout_view(request):
    logout(request)
    return redirect('login')
