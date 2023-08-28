from django import forms
from .models import Photographer


class AddPhotographForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = '__all__'