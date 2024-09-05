from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Subject
# Create your views here.

def ga_module(request):
    mysubjects = Subject.objects.all().values()
    template = loader.get_template('all_subjects.html')
    context = {
        'mysubjects' : mysubjects,
    }
    return HttpResponse(template.render(context, request))

def subject_details(request, id):
    mysubjects = Subject.objects.get(id=id)
    template = loader.get_template('subject_details.html')
    context = {
        'mysubjects': mysubjects,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits' : ['Apple', 'Cherry', 'Banana'],
    }
    return HttpResponse(template.render(context, request))