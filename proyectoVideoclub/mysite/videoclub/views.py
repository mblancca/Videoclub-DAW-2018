from django.shortcuts import render

# Create your views here.

from .models import Pelicula, Director, Actor, Genero

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    n_peliculas=Pelicula.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    n_directores=Director.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'Nº de peliculas':n_peliculas,'Nº de directores':n_directores},
    )

from django.views import generic

class catalogoPeliculas(generic.ListView):
    model = Pelicula
    paginate_by = 10

class infoPeli(generic.DetailView):
    model = Pelicula

def verPelicula(request):
    nombre_pelicula=Pelicula.objects.filter(nombre__exact='Gladiator')
    return render(
        request,
        'verPelicula.html', 
        context={'nombre_pelicula':nombre_pelicula},
    )
