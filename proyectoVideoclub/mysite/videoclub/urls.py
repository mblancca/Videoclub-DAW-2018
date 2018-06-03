from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula-info/<int:pk>', views.catalogoPeliculas.as_view(), name='catalogoPeliculas'),
    path('pelicula/<int:pk>', views.verPelicula, name='verPelicula'),
]
