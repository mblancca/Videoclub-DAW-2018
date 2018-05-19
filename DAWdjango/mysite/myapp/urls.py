from django.urls import path

from . import views
from django.conf.urls import include, url
from myapp.views import SignUpView, BienvenidaView, SignInView, SignOutView

urlpatterns = [
	#path('', views.acceso, name='acceso'),
	path('index/', views.index, name='index'),
	url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
	url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
	url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
]