from django.shortcuts import render
from .models import Pelicula, Persona, InstanciaPelicula, Genero
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_peliculas=Pelicula.objects.all().count()
    num_instances=InstanciaPelicula.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=InstanciaPelicula.objects.filter(status__exact='a').count()
    num_directores=Persona.objects.count()  # El 'all()' esta implícito por defecto.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_peliculas':num_peliculas,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_directores':num_directores,
        'num_visits':num_visits}, # num_visits appended
    )

class PeliculaListView(LoginRequiredMixin,generic.ListView):
    model = Pelicula
    paginate_by = 1

class PeliculaDetailView(LoginRequiredMixin,generic.DetailView):
    model = Pelicula

def pelicula_detail_view(request,pk):
    try:
        pelicula_id=Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        raise Http404("Book does not exist")

    #pelicula_id=get_object_or_404(Pelicula, pk=pk)
    
    return render(
        request,
        'videoclub/pelicula_detail.html',
        context={'pelicula':pelicula_id,}
    )

class DirectorListView(LoginRequiredMixin,generic.ListView):
    model = Persona
    paginate_by = 1

class DirectorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Persona

def director_detail_view(request,pk):
    try:
        persona_id=Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        raise Http404("Director does not exist")

    #director_id=get_object_or_404(Pelicula, pk=pk)
    
    return render(
        request,
        'videoclub/director_detail.html',
        context={'persona':persona_id,}
    )



