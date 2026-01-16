from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AboutMe

def about_me(request):
  myaboutme = AboutMe.objects.all().values()
  template = loader.get_template('about-me.html')
  context = {
    'myaboutme': myaboutme,
  }
  return HttpResponse(template.render(context, request))

# def main(request):
#   template = loader.get_template('../templates/main.html')
#   return HttpResponse(template.render())