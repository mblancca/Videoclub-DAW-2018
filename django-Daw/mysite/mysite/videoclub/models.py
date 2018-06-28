from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

#####################################################

class Genero(models.Model):
    name = models.CharField(max_length=200, help_text="Introduzca un genero de película")    
    def __str__(self):        
        return self.name

#####################################################

class Persona(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    esDirector = models.CharField(max_length=2, default="no",help_text="si/no , en minusculas todo")
    
    def get_absolute_url(self):        
        return reverse('persona-detalle', args=[str(self.id)])    

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)        

#####################################################

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, blank=False, default="")
    url = models.CharField(max_length=200, blank=False, default="")
    descripcion = models.TextField(max_length=1000, default="", help_text="Introduce una descripcion para la película")
    año = models.DateField(null=True, blank=True)
    models.DateField(null=True, blank=True)
    director = models.ForeignKey(Persona, related_name='director',on_delete=models.SET_NULL, null=True)
    reparto = models.ForeignKey(Persona, related_name='reparto',on_delete=models.SET_NULL, null=True)
    urlPortada = models.CharField(max_length=200, default="")
    genero = models.ManyToManyField(Genero, help_text="Selecciona un género para esta pelicula")
    valoracion = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo    
    
    def get_absolute_url(self):
        return reverse('pelicula-detalle', args=[str(self.id)])

#####################################################