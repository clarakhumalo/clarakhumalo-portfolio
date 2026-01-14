from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('skills-and-proficiencies/', views.skills_and_proficiencies, name='skills_and_proficiencies'),
]
