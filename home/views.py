from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def register_request(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "Registration successful.")
            return redirect("/")
        else:
            messages.error(request, form.errors)
    context = {
        "register_form": form,
        'user': request.user,
    }
    return render(request, "home/register.html", context)


def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'Welcome back {user.username}')
            return redirect('/')
        else:
            messages.error(request, 'Invalid login details, please try again.')
    form = AuthenticationForm()
    context = {
        'form': form
        }
    return render(request, 'home/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
