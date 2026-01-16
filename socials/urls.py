from django.urls import path
from . import views

urlpatterns = [
    path('', views.socials, name='socials'),    
]
