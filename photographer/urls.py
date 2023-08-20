from django.urls import path
from . import views

urlpatterns = [
    path('photographer-profile/', views.photographer_profile, name='photographer-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
]