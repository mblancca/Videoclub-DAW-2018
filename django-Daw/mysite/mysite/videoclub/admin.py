from django.contrib import admin

# Register your models here.

from .models import Director, Genero, Pelicula, InstanciaPelicula

admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(InstanciaPelicula)