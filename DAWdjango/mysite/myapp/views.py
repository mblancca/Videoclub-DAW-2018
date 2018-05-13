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

def form(request):
	context = {}
	return render(request, "myapp/form.html", context)

texts = []

def process_form(request):
	context = {}
	if request.method == 'POST':
		input_text = request.POST['input_text']
		texts.append(input_text)
		context['texts'] = texts
	return render(request, "myapp/process_form.html", context)
