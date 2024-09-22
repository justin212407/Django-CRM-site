from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record  

def home(request):
    records = Record.objects.all()  # Fetch records here
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, 'There was an Error Logging In, Please Try Again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out")
	return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered! Welcome!!")
                return redirect('home')  # Ensure a response is returned
            else:
                messages.error(request, "Error in form submission. Please try again.")
        else:
            messages.error(request, "Invalid form data. Please correct the errors and try again.")
    else:
        # Create an empty form if the request is not POST
        form = SignUpForm()

    # Always return an HttpResponse, rendering the form
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		#Look up records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record': customer_record})
	else:
		messages.error(request, "You must be logged in to view the page.")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Succesfully")
		return redirect('home')
	else:
		messages.error(request, "You must be Logged in to delete a Record.")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added.")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.error(request, "You must be Logged In.")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Updated.")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.error(request, "You must be Logged In.")
		return redirect('home')
