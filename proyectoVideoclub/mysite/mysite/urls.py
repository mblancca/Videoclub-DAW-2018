"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #pagina home. catalogo peliculas. se pueden filtrar por nombre, genero y/o director (y actor). ¿mostrar info?
    path('videoclub/', include('videoclub.urls')), 
    #ventana en la que se visualiza una pelicula especifica
    path('videoclub/pelicula/<int:pk>', include('videoclub.urls')),
    #muestra info de una pelicula especifica
    path('videoclub/pelicula-info/<int:pk>', include('videoclub.urls')), 
    path('', RedirectView.as_view(url='/videoclub/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
