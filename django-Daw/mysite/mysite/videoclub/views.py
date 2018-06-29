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
        genero__name__icontains='genero1').order_by('-id')[:2]  # Coge las 2 primeras
    listaPeliculas2 = Pelicula.objects.all().filter(
        genero__name__icontains='genero1').order_by('id')[:2]  # Coge las 2 ultimas

    listaPeliculas3 = Pelicula.objects.all().filter(
        genero__name__icontains='accion').order_by('-id')[:2]  # Coge las 2 primeras
    listaPeliculas4 = Pelicula.objects.all().filter(
        genero__name__icontains='accion').order_by('id')[:2]  # Coge las 2 ultimas

    numero_visitas = request.session.get('numero_visitas', 0)
    request.session['numero_visitas'] = numero_visitas+1

    return render(
        request,
        'index.html',
        context={'listaPeliculas1': listaPeliculas1,
                 'listaPeliculas2': listaPeliculas2,
                 'listaPeliculas3': listaPeliculas3,
                 'listaPeliculas4': listaPeliculas4}
    )


class PeliculaListView(LoginRequiredMixin, generic.ListView):
    model = Pelicula
    paginate_by = 10

    def get_queryset(self):
        listaDePeliculas = self.model.objects.filter(
            genero__name__icontains='genero1')
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
    paginate_by = 10
    template_name = 'videoclub/director_list.html'

    def get_queryset(self):
        listaDeDirectores = self.model.objects.filter(
            esDirector__icontains='si')
        return listaDeDirectores

# Reparto de actores


class ActorListView(LoginRequiredMixin, generic.ListView):
    model = Persona
    paginate_by = 10
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
        peliculas = Pelicula.objects.filter(titulo__icontains=q)
        return render(request, 'videoclub/search_results.html',
                      {'peliculas': peliculas, 'query': q})
    else:
        return render(request, 'videoclub/search_error.html')

# BAD!


def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)
