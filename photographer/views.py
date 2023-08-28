from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Photographer
from products.models import Product
from .forms import AddPhotographForm


def photographer_profile(request):
    """ A view to return the photographer profile page """

    return render(request, 'photographer/photographer-profile.html')


@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = Photographer.objects.get(user=user)
    except Photographer.DoesNotExist:
        # Create a profile if it doesn't exist
        profile = Photographer(user=user)
        profile.save()

    if request.method == 'POST':
        # Update the profile fields with the submitted data
        profile.name = request.POST['name']
        profile.bio = request.POST['bio']
        profile.location = request.POST['location']
        profile.website = request.POST['website']
        profile.social_facebook = request.POST['social_facebook']
        profile.social_instagram = request.POST['social_instagram']
        profile.phone = request.POST['phone']

        # Check if a new profile picture was uploaded
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        # Save the changes
        profile.save()
        user.email = request.POST['email']
        user.save()

        return redirect('photographer-profile')

    return render(request, 'photographer/edit-profile.html', {'user': user})


# Create your views here.


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

    context = {
        'photographer': photographer,
    }

    return render(request, 'photographer/photographer-profile.html', context)


def add_photographer(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = AddPhotographForm(request.POST, request.FILES)
        if form.is_valid():
            photographer = form.save(commit=False)
            photographer.user = request.user
            photographer.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = AddPhotographForm()
    form = AddPhotographForm()
    template = 'photographer/add_photographer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
