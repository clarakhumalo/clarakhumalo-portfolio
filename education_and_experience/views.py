from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import EducationAndExperience

def education_and_experience(request):
  myeducationandexperience = EducationAndExperience.objects.all().values()
  template = loader.get_template('education-and-experience.html')
  context = {
    'myeducationandexperience': myeducationandexperience,
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