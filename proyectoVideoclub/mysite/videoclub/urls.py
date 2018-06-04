from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.catalogoPeliculas.as_view(), name='catalogoPeliculas'),
    #url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    path('videoclub/<int:pk>',views.peliculaInfo.as_view(), name='pelicula-info'),
	path('videoclub/<int:pk>/play', views.verPelicula, name='verPelicula'),
]
