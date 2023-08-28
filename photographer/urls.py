from django.urls import path
from . import views

urlpatterns = [
    path('photographer-profile/<int:photographer_id>/', views.photographer_profile,
         name='photographer-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('', views.all_photographers, name='photographers'),
    path('<int:photographer_id>/', views.photographer_page,
         name='photographer_page'),
    path('add_photographer/', views.add_photographer, name='add_photographer'),
    path('edit_photographer/<int:photographer_id>', views.edit_photographer, name='edit_photographer'),
]
