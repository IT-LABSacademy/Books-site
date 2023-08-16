from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import UsersModel
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


class RegisterPageView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['firstname']
             
            try:
                # Create a new user object
                user = UsersModel.objects.create_user(username=username, password=password, first_name=first_name)
                
                # Authenticate and log in the user
                user = authenticate(request, username=username, password=password)
                login(request, user)
                
                return redirect('home')  # Redirect to the homepage or any other desired page
        
            except IntegrityError:
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'users/register.html', {'error_message': error_message})
    
    
        return render(request, 'users/register.html')
    


def log_out(request):
    logout(request)
    return redirect("home")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'users/login.html')
