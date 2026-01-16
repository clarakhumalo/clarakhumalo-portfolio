from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home

def main(request):
  myhome = Home.objects.all()
  return render (request, 'main.html', {'myhome': myhome})