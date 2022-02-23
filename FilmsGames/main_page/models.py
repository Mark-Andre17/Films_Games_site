from django.db import models
from django.urls import reverse


class Actor(models.Model):
    name = models.TextField(verbose_name='Актер')
    photo = models.ImageField(verbose_name='Фото актера', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Producer(models.Model):
    name = models.TextField(verbose_name='Режиссер')
    photo = models.ImageField(verbose_name='Фото режиссера', upload_to='producers/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Genre(models.Model):
    name = models.TextField(verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(models.Model):
    name = models.TextField(verbose_name='Название фильма')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(verbose_name='Описание фильма')
    year = models.IntegerField(verbose_name='Год выхода фильма')
    raiting_IMDB = models.FloatField(verbose_name='Рейтинг IMDB', null=True, blank=True)
    raiting_KP = models.FloatField(verbose_name='Рейтинг Кинопоиска', null=True, blank=True)
    poster = models.ImageField(verbose_name='Постер фильма', upload_to='poster/')
    budget = models.PositiveIntegerField(verbose_name='Бюджет')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actors')
    producers = models.ManyToManyField(Producer, verbose_name='режиссеры', related_name='film_producers')
    genre = models.ManyToManyField(Genre, verbose_name='жанры', related_name='film_genres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def get_absolute_url(self):
        return reverse('films', kwargs={'film_url': self.slug})


class Studio(models.Model):
    name = models.TextField(verbose_name='Название студии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'


class GameGenre(models.Model):
    name = models.TextField(verbose_name='Жанр игры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Platform(models.Model):
    name = models.TextField(verbose_name='Платформа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class Game(models.Model):
    name = models.TextField(verbose_name='Название игры')
    date = models.DateField(verbose_name='Дата выхода игры')
    slug = models.SlugField(verbose_name='URL', max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(verbose_name='Описание игры')
    poster = models.ImageField(verbose_name='Постер игры', upload_to='games/')
    raiting = models.FloatField(verbose_name='Рейтинг Metacritic', null=True, blank=True)
    studio = models.ForeignKey(Studio, verbose_name='Студия игры', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(GameGenre, verbose_name='Жанр игры', null=True, blank=True, on_delete=models.SET_NULL)
    platform = models.ManyToManyField(Platform, verbose_name='Платформа игры', related_name='game_platform')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def get_absolute_url(self):
        return reverse('games', kwargs={'game_url': self.slug})
