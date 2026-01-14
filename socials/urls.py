from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('socials/', views.socials, name='socials'),
    path('testing/', views.testing, name='testing'),    
]
