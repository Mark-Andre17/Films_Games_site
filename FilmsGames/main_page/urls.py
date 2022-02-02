from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('films/', film, name='films'),
    path('films/<slug:film_slug>/', film_info, name='film_info')
]
