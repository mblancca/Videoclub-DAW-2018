from django.shortcuts import render
from .models import Pelicula, Director, InstanciaPelicula, Genero
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
    num_books=Pelicula.objects.all().count()
    num_instances=InstanciaPelicula.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=InstanciaPelicula.objects.filter(status__exact='a').count()
    num_authors=Director.objects.count()  # El 'all()' esta implícito por defecto.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
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
    model = Director
    paginate_by = 1

class DirectorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Director

def director_detail_view(request,pk):
    try:
        director_id=Director.objects.get(pk=pk)
    except Director.DoesNotExist:
        raise Http404("Director does not exist")

    #director_id=get_object_or_404(Pelicula, pk=pk)
    
    return render(
        request,
        'videoclub/director_detail.html',
        context={'director':director_id,}
    )



