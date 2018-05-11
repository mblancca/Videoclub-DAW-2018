from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

visit_count = 0

def index(request):
	global visit_count
	visit_count += 1
	template=loader.get_template("myapp/index.html")
	context = {
		'name' : 'Pepe',
		'visit_count' : visit_count,
	}
	return HttpResponse(template.render(context, request))
	
def other(request):
	template=loader.get_template("myapp/other.html")
	context = {
		'item_list' : [
			'Red',
			'Green',
			'Blue'
		]
	}
	return HttpResponse(template.render(context, request))