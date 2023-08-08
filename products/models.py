from django.db import models
from photographer.models import Photographer


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()

    def __str__(self):
        return self.name
