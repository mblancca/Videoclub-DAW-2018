from django.shortcuts import render
from .models import Pelicula, Persona, Genero
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import operator
from django.http import HttpResponse

# Create your views here.


@login_required
def index(request):
    listaPeliculas1 = Pelicula.objects.all().filter(
        genero__name__icontains='Ciencia ficción').order_by('-id')[:4]  # Coge las 4 primeras
    listaPeliculas2 = Pelicula.objects.all().filter(
        genero__name__icontains='Ciencia ficción').order_by('id')[:4]  # Coge las 4 ultimas    
    listaPeliculas5 = Pelicula.objects.all().filter(
        genero__name__icontains='Acción').order_by('-id')[:4]  # Coge las 2 primeras
    listaPeliculas6 = Pelicula.objects.all().filter(
        genero__name__icontains='Acción').order_by('id')[:4]  # Coge las 2 ultimas
    
    listaPeliculas7 = Pelicula.objects.all().filter(
        genero__name__icontains='Drama').order_by('-id')[:4]  # Coge las 2 primeras
    listaPeliculas8 = Pelicula.objects.all().filter(
        genero__name__icontains='Drama').order_by('id')[:4]  # Coge las 2 ultimas

    numero_visitas = request.session.get('numero_visitas', 0)
    request.session['numero_visitas'] = numero_visitas+1

    return render(
        request,
        'index.html',
        context={'listaPeliculas1': listaPeliculas1,
                 'listaPeliculas2': listaPeliculas2,                 
                 'listaPeliculas5': listaPeliculas5,
                 'listaPeliculas6': listaPeliculas6,
                 'listaPeliculas7': listaPeliculas7,
                 'listaPeliculas8': listaPeliculas8}
    )


class PeliculaListView(LoginRequiredMixin, generic.ListView):
    model = Pelicula
    paginate_by = 4

    def get_queryset(self):
        listaDePeliculas = self.model.objects.all()
        return listaDePeliculas


class PeliculaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Pelicula


def pelicula_detail_view(request, pk):
    try:
        pelicula_id = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        raise Http404("Pelicula does not exist")

    return render(
        request,
        'videoclub/pelicula_detail.html',
        context={'pelicula': pelicula_id, }
    )

# Reparto de Directores


class DirectorListView(LoginRequiredMixin, generic.ListView):
    model = Persona
    paginate_by = 4
    template_name = 'videoclub/director_list.html'

    def get_queryset(self):
        listaDeDirectores = self.model.objects.filter(
            esDirector__icontains='si')
        return listaDeDirectores

# Reparto de actores


class ActorListView(LoginRequiredMixin, generic.ListView):
    model = Persona
    paginate_by = 4
    template_name = 'videoclub/actor_list.html'

    def get_queryset(self):
        listaDeActores = self.model.objects.filter(esDirector__icontains='no')
        return listaDeActores


class PersonaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Persona
    template_name = 'videoclub/person_detail.html'

# BuscarPeliculas


def search_form(request):
    return render(request, 'videoclub/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        contadorPeliculas = Pelicula.objects.filter(
            titulo__icontains=q).count()
        contadorPersonas = Persona.objects.filter(nombre__icontains=q).count()
        contadorGeneros = Genero.objects.filter(name__icontains=q).count()

        if contadorPeliculas != 0:
            peliculas = Pelicula.objects.filter(titulo__icontains=q)
            return render(request, 'videoclub/search_results.html',
                          {'peliculas': peliculas, 'query': q})
        elif contadorPersonas != 0:
            personas = Persona.objects.filter(nombre__icontains=q)
            return render(request, 'videoclub/search_results.html',
                          {'personas': personas, 'query': q})        
        else:
            return render(request, 'videoclub/search_results.html',
                          {'query': q})

    else:
        return render(request, 'videoclub/search_error.html')

# BAD!
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)