from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home/index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="home/register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        email = request.POST['email'],
        password = request.POST['password'],
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user),
            messages.success(request, f'Welcome back {{user.username}}'),
            return redirect('home/index.html'),
        else:
            messages.error(request, 'Invalid email or password, please try again.')

    return render(request, 'home/login.html')

    
	# 	form = AuthenticationForm(request, data=request.POST)
	# 	if form.is_valid():
	# 		username = form.cleaned_data.get('username')
	# 		password = form.cleaned_data.get('password')
	# 		user = authenticate(username=username, password=password)
	# 		if user is not None:
	# 			login(request, user)
	# 			messages.info(request, f"You are now logged in as {username}.")
	# 			return redirect("home/index.html")
	# 		else:
	# 			messages.error(request, "Invalid username or password.")
	# 	else:
	# 		messages.error(request, "Invalid username or password.")
	# form = AuthenticationForm()
	# return render(request=request, template_name="home/login.html", context={"login_form":form})
