from django.db import models, transaction
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from photographer.models import Photographer


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    class Meta:
        verbose_name_plural = 'SubCategories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField('Category')
    subcategory = models.ManyToManyField('SubCategory')
    photographer = models.ForeignKey(
        Photographer, on_delete=models.CASCADE, default="")
    sku = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='S')

    # Logic to generate a new unique SKU with new product creation
    @classmethod
    def generate_sku(cls):
        with transaction.atomic():
            last_sku_instance = cls.objects.select_for_update().order_by('-id').first()  # noqa

            if last_sku_instance:
                last_sku = last_sku_instance.sku
                counter = int(last_sku[6:]) + 1
                new_sku = f'PROD{counter:06}'
            else:
                new_sku = 'PROD000001'

            return new_sku

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Product)
def generate_sku_on_save(sender, instance, **kwargs):
    if not instance.sku:
        instance.sku = instance.generate_sku()
