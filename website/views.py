from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')

def signup_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect('about')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please login or use another email.")
            return redirect('about')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  
        return redirect('home')

    return render(request, 'signup.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('home')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.error(request, "Invalid email or password")
    return redirect('dashboard')


def logout_page(request):
    logout(request)  
    return redirect('home')  

# views.py
from django.contrib.auth.decorators import login_required

@login_required  # user must be logged in
def dashboard_page(request):
    return render(request, 'dashboard.html')

@login_required
def feature_notes(request):
    return render(request, 'notes.html')