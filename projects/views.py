from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

def projects(request):
  myprojects = Project.objects.all().values()
  template = loader.get_template('projects.html')
  context = {
    'myprojects': myprojects,
  }
  return HttpResponse(template.render(context, request))