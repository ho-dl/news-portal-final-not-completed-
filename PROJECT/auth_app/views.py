from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import  User
from django.contrib import messages





# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        email = request.POST.get('email')
    
        
        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')

            # Create the user
            user = User.objects.create_user(
                username=username, 
                password=password,
                is_user = True,
              
    
                email=email,
             
                )
            user.save()
            
            messages.success(request, 'Registered Successfully and logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

    return render(request, 'register.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')