from django import forms
from .models import Photographer


class AddPhotographForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = (
            'name',
            'profile_picture',
            'bio',
            'location',
            'website',
            'social_facebook',
            'social_instagram',
            'email',
            'phone'
        )
