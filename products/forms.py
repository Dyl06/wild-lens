from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, SubCategory
from photographer.models import Photographer


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'category',
            'subcategory',
            'photographer',
            'name',
            'description',
            'price',
            'image',
        )

    image = forms.ImageField(
                                label='Image',
                                required=True,
                                widget=CustomClearableFileInput
                            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assign choices for category, subcategory, and photographer fields
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]  # noqa
        self.fields['subcategory'].choices = [(subcategory.id, subcategory.name) for subcategory in SubCategory.objects.all()]  # noqa
        self.fields['photographer'].choices = [(photographer.id, photographer.name) for photographer in Photographer.objects.all()]  # noqa

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
