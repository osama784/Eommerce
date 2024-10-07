from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from .forms import UserForm, LoginForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('products:home')
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', reverse('products:home'))
                return redirect(next_url)

            
    return render(request, 'login.html')

@require_http_methods(['GET', 'POST'])
def register_user(request):
    if request.user.is_authenticated:
        return redirect('products:home')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            login(request, instance)
            return redirect("products:home")
        
    return render(request, 'sign-up.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('products:home')

@login_required
def save_profile_info(request):
    city = request.POST.get('city', None)
    country = request.POST.get('country', None)
    phone_number = request.POST.get('phone_number', None)
    profile = request.user.profile
    profile.address = f'{country}, {city}'
    profile.phone_number = phone_number
    profile.save()
    return redirect('services:dashboard')

@login_required
def save_names(request):
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    email = request.POST.get('email', None)
    user = request.user
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.profile.image = request.FILES.get('image')
    user.profile.save()
    user.save()
    return redirect('services:dashboard')
    