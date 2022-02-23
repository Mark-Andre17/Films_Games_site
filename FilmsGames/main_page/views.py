from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm

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


def game(request):
    games = Game.objects.all()
    context = {'tittle': 'Игры', 'games': games}
    return render(request, 'main_page/games.html', context)


def game_info(request, game_slug):
    games = Game.objects.get(slug=game_slug)
    context = {'tittle': 'Игры', 'games': games}
    return render(request, 'main_page/game_info.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            remember_me = form.cleaned_data['remember_me']
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main_page/login.html', {'tittle': 'Вход', 'form': form})


@login_required
def dashboard(request):
    return render(request, 'main_page/dashboard.html', {'tittle': 'Личный кабинет', 'section': 'dashboard'})


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'main_page/registration_done.html', {'tittle': 'Регистрация', 'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main_page/registration.html', {'tittle': 'Регистрация', 'user_form': user_form})
