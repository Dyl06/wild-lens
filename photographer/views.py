from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Photographer
from products.models import Product
from .forms import AddPhotographForm
from django.contrib.auth.models import Group


def is_photographer(request):
    GROUP_NAME_FOR_PHOTOGRAPHERS = "Photographers"
    user_is_photographer = request.user.groups.filter(name=GROUP_NAME_FOR_PHOTOGRAPHERS).exists()
    return user_is_photographer


def photographer_profile(request):
    """ A view to return the photographer profile page """

    return render(request, 'photographer/photographer-profile.html')


def all_photographers(request):
    """ A view to show all the photographers on the site """

    photographers = Photographer.objects.all()

    context = {
        'photographers': photographers,
    }

    return render(request, 'photographer/photographers.html', context)


def photographer_page(request, photographer_id):
    """ A view to show the individual photographer profile page """

    photographer = get_object_or_404(Photographer, pk=photographer_id)

    two_photos = Product.objects.filter(photographer=photographer)[:2]

    context = {
        'photographer': photographer,
        'two_photos': two_photos
    }

    return render(request, 'photographer/photographer-profile.html', context)

@login_required(login_url='login')
def add_photographer(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = AddPhotographForm(request.POST, request.FILES)
        if form.is_valid():
            photographer = form.save(commit=False)
            photographer.user = request.user
            photographer.save()

            photographers_group = Group.objects.filter(name='Photographers')
            request.user.groups.set(photographers_group)
            request.user.save()

            messages.info(request, 'Successfully added photographer!')
            return redirect(reverse('add_photographer'))
        else:
            messages.error(request, 'Failed to add photographer. Please ensure the form is valid.')
    else:
        form = AddPhotographForm()
    form = AddPhotographForm()
    template = 'photographer/add_photographer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# @login_required(login_url='login')
def edit_photographer(request):
    """ Edit a photographer profile """

    photographer = get_object_or_404(Photographer, user=request.user)
    form = AddPhotographForm(instance=photographer)
    if request.user == photographer.user:
        if request.method == 'POST':
            form = AddPhotographForm(request.POST, request.FILES, instance=photographer)
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully updated profile!')
                return redirect(reverse('photographers'))
            else:
                messages.error(request, 'Failed to update profile. Please ensure the form is valid.')
        else:
            form = AddPhotographForm(instance=photographer)
            messages.info(request, f'You are editing {photographer.name}')

    template = 'photographer/edit_photographer.html'
    context = {
        'photographer': photographer,
        'form': form,

    }

    return render(request, template, context)