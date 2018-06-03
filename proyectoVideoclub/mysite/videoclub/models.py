from django.db import models

# Create your models here.


class Genero(models.Model):
    """
    Modelo que representa un género cinematográfico.
    """
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=200, help_text="Escribe un género cinematográfico.")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name


# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

class Pelicula(models.Model):
    """
    Modelo que representa una pelicula.
    """
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=200, help_text="Nombre original de la película")

    URLcontenido = models.CharField(max_length=200)

    descripcion = models.TextField(max_length=1000, help_text="Descripción de la película")

    anyo = models.DateField(help_text="Año del estreno de la película")

    genero = models.ManyToManyField(Genero, help_text='Género cinematográfico en el que se clasifica la película')

    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True, help_text='Director de la película')
    
    reparto = models.ManyToManyField('Actor', help_text='Actores que aparecen oficialmente en la película')

    URLportada = models.CharField(max_length=200)
    
    valoracion = models.DecimalField(decimal_places=1,max_digits=2)

    def __str__(self):
        """
        String que representa al objeto Pelicula
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Pelicula
        """
        return reverse('pelicula-detail', args=[str(self.id)])

class Actor(models.Model):
    """
    Modelo que representa un actor
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un actor.
        """
        return reverse('actor-detail', args=[str(self.id)])

class Director(models.Model):
    """
    Modelo que representa un director
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    es_actor = models.BooleanField()
    
    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un director.
        """
        return reverse('director-detail', args=[str(self.id)])

    