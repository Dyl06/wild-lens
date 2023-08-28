from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_page, name='product_page'),
    path('profile', views.all_products, name='profile'),
    path('add/', views.add_product, name='add_product'),
]
