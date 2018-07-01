from django.conf.urls import url

from . import views
from django.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^peliculas/$', views.PeliculaListView.as_view(), name='peliculas'),
    url(r'^pelicula/(?P<pk>\d+)$', views.PeliculaDetailView.as_view(), name='pelicula-detalle'),
    url(r'^directores/$', views.DirectorListView.as_view(), name='directores'),
    url(r'^actores/$', views.ActorListView.as_view(), name='actores'),
    url(r'^personas/(?P<pk>\d+)$', views.PersonaDetailView.as_view(), name='persona-detalle'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search, name="search"),
]