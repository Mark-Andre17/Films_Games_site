from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
    {'tittle': 'Фильмы', 'url_name': 'films'},
    {'tittle': 'Игры', 'url_name': 'games'},
    {'tittle': 'Регистрация', 'url_name': 'registration'},
    {'tittle': 'Вход', 'url_name': 'login'}
]


def main(request):
    context = {'tittle': 'Главная страница', 'menu': menu}
    return render(request, 'main_page/main.html', context)


def film(request):
    films = Film.objects.all()
    context = {'tittle': 'Фильмы', 'films': films}
    return render(request, 'main_page/films.html', context)


def film_info(request, film_slug):
    films = Film.objects.get(slug=film_slug)
    context = {'tittle': 'Фильмы', 'films': films}
    return render(request, 'main_page/film_info.html', context)
