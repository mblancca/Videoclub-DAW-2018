from django.contrib import admin

# Register your models here.

from .models import Persona, Genero, Pelicula

admin.site.register(Pelicula)
admin.site.register(Persona)
admin.site.register(Genero)
