from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Socials

def socials(request):
  mysocials = Socials.objects.all().values()
  template = loader.get_template('socials.html')
  context = {
    'mysocials': mysocials,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('C:/Users/De/Documents/Side Projects/HTML & CSS/clara_khumalo_dev_portfolio/templates/main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('testing.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))