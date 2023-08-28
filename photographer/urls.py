from django.urls import path
from . import views

urlpatterns = [
    path('photographer-profile/', views.photographer_profile, name='photographer-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('', views.all_photographers, name='photographers'),
    path('<photographer_id>', views.photographer_page, name='photographer_page'),
    path('add_photograph', views.add_photograph, name='add_photograph'),
]
