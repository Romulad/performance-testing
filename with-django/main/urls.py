from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home-with-variable/', views.home_with_variable, name='home_with_variable'),
    path('ping/', views.ping, name='ping'),
]
