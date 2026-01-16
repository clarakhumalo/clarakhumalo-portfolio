from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SkillsAndProficiencies

def skills_and_proficiencies(request):
  myskillsandproficiencies = SkillsAndProficiencies.objects.all().values()
  template = loader.get_template('skills-and-proficiencies.html')
  context = {
    'myskillsandproficiencies': myskillsandproficiencies,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('../templates/main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('404.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))