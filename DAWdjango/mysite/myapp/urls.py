from django.urls import path

from . import views
from django.conf.urls import include

urlpatterns = [
	path('',views.index, name='index'),
	path('other/test',views.other, name='other'),
	path('form',views.form,name='form'),
	path('process_form',views.process_form,name='process_form')
]