from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

#####################################################

class Genero(models.Model):
    """
    Modelo que representa un género cinematográfico (p. ej. ciencia ficción, poesía, etc.).
    """
    nombre = models.CharField(max_length=200, help_text="Introduzca un genero de película (Ciencia ficcion, Comedia, etc.)")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

#####################################################

class Pelicula(models.Model):
    """
    Modelo que representa una película (pero no un Ejemplar específico).
    """

    titulo = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un Pelicula tiene un solo Director, pero el mismo Director puede haber escrito muchos Peliculas.
    # 'Director' es un string, en vez de un objeto, porque la clase Director aún no ha sido declarada.

    sumario = models.TextField(max_length=1000, help_text="Enter a brief description of the movie")
    
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genero = models.ManyToManyField(Genero, help_text="Selecciona un género para esta pelicula")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.
    
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.titulo
    
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('pelicula-detalle', args=[str(self.id)])

#####################################################

import uuid # Requerida para las instancias de peliculas únicas

class InstanciaPelicula(models.Model):
    """
    Modelo que representa una copia específica de una pelicula (i.e. que puede ser prestado por el videoclub).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta pelicula en particular en todo el videoclub")
    pelicula = models.ForeignKey('Pelicula', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        #proximamente, en mantenimiento, reservado, disponible, ...
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)

#####################################################

class Director(models.Model):
    """
    Modelo que representa un director
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    fecha_de_defuncion = models.DateField('Fallecido', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un director.
        """
        return reverse('director-detalle', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.apellido, self.nombre)