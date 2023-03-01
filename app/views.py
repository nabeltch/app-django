from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def machine(request):
  template = loader.get_template('machine.html')
  return HttpResponse(template.render())
