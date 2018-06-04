from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    #url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url('videoclub/<int:pk>',views.catalogoPeliculas.as_view(), name='catalogoPeliculas'),
	url('videoclub/<int:pk>/play', views.verPelicula, name='verPelicula'),
]
