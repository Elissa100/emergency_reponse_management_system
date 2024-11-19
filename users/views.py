from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import CustomUser
from django.conf import settings

def home(request):
    """Home page view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    print("Template paths:", settings.TEMPLATES)
    return render(request, 'users/home.html')

def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'users/login.html')

def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    """User dashboard view"""
    return render(request, 'users/dashboard.html')

@login_required
def user_profile(request):
    """User profile view"""
    return render(request, 'users/profile.html')

@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def manage_users(request):
    """Admin view for managing users"""
    if not request.user.user_type == 'ADMIN':
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('dashboard')
        
    users = CustomUser.objects.all()
    return render(request, 'users/manage_users.html', {'users': users})

@login_required
def edit_user(request, user_id):
    """Admin view to edit a user"""
    if not request.user.user_type == 'ADMIN':
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('dashboard')
    
    user = CustomUser.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('manage_users')
    else:
        form = UserRegistrationForm(instance=user)
    
    return render(request, 'users/edit_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    """Admin view to delete a user"""
    if not request.user.user_type == 'ADMIN':
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('dashboard')

    user = CustomUser.objects.get(id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('manage_users')

