from django.urls import path
from . import views

urlpatterns = [
    path('photographer/<int:photographer_id>/', views.photographer_profile,
         name='photographer-profile'),
    path('', views.all_photographers, name='photographers'),
    path('<int:photographer_id>/', views.photographer_page,
         name='photographer_page'),
    path('add_photographer/', views.add_photographer, name='add_photographer'),
    path('edit_photographer/', views.edit_photographer, name='edit_photographer'),
]
