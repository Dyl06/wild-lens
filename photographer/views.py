from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Photographer


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
