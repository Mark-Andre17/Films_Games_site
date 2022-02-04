from django.contrib import admin
from .models import *


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Actor)
admin.site.register(Producer)
admin.site.register(Genre)
admin.site.register(Film, FilmAdmin)

