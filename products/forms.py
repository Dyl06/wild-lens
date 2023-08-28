from django import forms
from .models import Product, Category, SubCategory
from photographer.models import Photographer


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assign choices for category, subcategory, and photographer fields
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]
        self.fields['subcategory'].choices = [(subcategory.id, subcategory.name) for subcategory in SubCategory.objects.all()]
        self.fields['photographer'].choices = [(photographer.id, photographer.name) for photographer in Photographer.objects.all()]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
