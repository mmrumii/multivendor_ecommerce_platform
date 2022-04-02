from django.urls import path

from . import views

app_name = 'dailybazar'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dailycost_id>/', views.detail, name='detail'),
]