from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def subjects(request):
    template = loader.get_template('subjects.html')
    return HttpResponse(template.render())

def teachers(request):
    template = loader.get_template('teachers.html')
    return HttpResponse(template.render())

def rooms(request):
    template = loader.get_template('rooms.html')
    return HttpResponse(template.render())