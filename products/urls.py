from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('all/', views.products, name='all_products'),
    path('<int:product_id>/', views.detail, name='detail'),
]