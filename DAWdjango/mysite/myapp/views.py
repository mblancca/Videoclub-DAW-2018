from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def prueba(request):
    template = loader.get_template("myapp/Index.html")
    return HttpResponse(template.render())
