from django.db import models
from django.urls import reverse
#####################################################

class Genero(models.Model):
    name = models.CharField(max_length=200, help_text="Introduzca un género de película")    
    def __str__(self):        
        return self.name

#####################################################

class Persona(models.Model):
    nombre = models.CharField(max_length=100, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    esDirector = models.CharField(max_length=2, default="no",help_text="si/no , en minusculas todo")
    urlFoto = models.CharField(max_length=200, blank=False, default="https://www.w3schools.com/css/img_avatar.png")
       
    def get_absolute_url(self):        
        return reverse('persona-detalle', args=[str(self.id)])
    
    def get_foto(self):
        return self.urlFoto

    def __str__(self):
        return self.nombre       

#####################################################

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, blank=False, default="")
    url = models.CharField(max_length=200, blank=False, default="")
    descripcion = models.TextField(max_length=1000, default="", help_text="Introduce una descripcion para la película")
    año = models.DateField(null=True, blank=True)
    models.DateField(null=True, blank=True)
    director = models.ForeignKey(Persona, related_name='director',on_delete=models.SET_NULL, null=True)
    reparto = models.ManyToManyField(Persona)
    urlPortada = models.CharField(max_length=200, default="")
    genero = models.ManyToManyField(Genero, help_text="Selecciona un género para esta pelicula")
    valoracion = models.PositiveIntegerField(help_text="Valor de 0-100")

    def __str__(self):
        return self.titulo    
    
    def get_portada(self):
        return self.urlPortada

    def get_url(self):
        return self.url

    def get_genero(self):
        return self.genero

    def get_absolute_url(self):
        return reverse('pelicula-detalle', args=[str(self.id)])

#####################################################