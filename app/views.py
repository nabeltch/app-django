from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from .machines import plc_data

def index(request):
  template = loader.get_template('index.html')
  context={
    'file':test(),
    'file 1':test,
  }
  return HttpResponse(template.render(context,request))

def machine(request):
  # template = loader.get_template('machine.html')
  # context = {
  #   'tags': cars,
  #  }
  return render(request, 'machine.html', {"list": list})
  # return HttpResponse(template.render(context,request))

def get_data(request):
    return JsonResponse(plc_data('03'),safe=False)

def data(request):
  template = loader.get_template('data.html')
  return HttpResponse(template.render())

def plc(request):
   return JsonResponse(plc_data('03'),safe=False)

def test(request):
   data=[1,2,3,4]
   return JsonResponse(data,safe=False)

