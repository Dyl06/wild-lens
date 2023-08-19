from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("register", views.register_request, name="register"),
    path("login", views.register_request, name="login"),
]
