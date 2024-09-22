from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        print("Form submitted!")  # Check if form is being submitted
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debug the form data
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Login successful!")  # Confirm successful authentication
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            print("Login failed!")  # Confirm failed login
            messages.error(request, 'There was an Error Logging In, Please Try Again')
            return redirect('home')
    else:
        return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})