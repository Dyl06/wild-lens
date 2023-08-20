from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EditProfileForm


def photographer_profile(request):
    """ A view to return the photographer profile page """

    return render(request, 'photographer/photographer-profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('photographer-profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'photographer/edit-profile.html', {'form': form})