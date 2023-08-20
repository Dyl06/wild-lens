from django.contrib.auth.forms import UserChangeForm
from .models import Photographer


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Photographer
        fields = (
            'email',
            'name',
            'profile_picture',
            'bio',
            'location',
            'website',
            'social_facebook',
            'social_instagram',
            'phone',
        )