from django.contrib import admin

# Register your models here.
from .models import Genero, Pelicula, Director, Actor

admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Actor)