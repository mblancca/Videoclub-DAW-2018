from django.db import models

# Create your models here.


class Genero(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(
        max_length=200, help_text="Escribe un género de película.")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name


# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

class Pelicula(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """

    nombre = models.CharField(max_length=200)

    URLcontenido = models.CharField(max_length=200)

    descripcion = models.TextField(
        max_length=1000, help_text="Escribe una descripción de la película")

    URLcontenido = models.DateField()

    director = models.ForeignKey(
        'Director', on_delete=models.SET_NULL, null=True)
    
    reparto = models.ManyToManyField(
        'Actor', on_delete=models.SET_NULL, null=True)

    URLportada = models.CharField(max_length=200)
    
    valoracion = models.DecimalField()

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('pelicula-detail', args=[str(self.id)])

class Actor(models.Model):
    """
    Modelo que representa un autor
    """
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
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('actor-detail', args=[str(self.id)])

class Director(models.Model):
    """
    Modelo que representa un autor
    """
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
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('director-detail', args=[str(self.id)])

    