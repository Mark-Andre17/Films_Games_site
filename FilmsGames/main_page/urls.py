from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', main, name='home'),
    path('films/', film, name='films'),
    path('films/<slug:film_slug>/', film_info, name='film_info'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', registration, name='registration'),
    path('dashboard/', dashboard, name='dashboard')
]
