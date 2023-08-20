from django.db import models
from django.contrib.auth.models import User


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='photographer_profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    social_facebook = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

 
