from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def login(request):
    template = loader.get_template("myapp/login.html")
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template("myapp/index.html")
    return HttpResponse(template.render())
