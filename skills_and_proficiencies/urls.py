from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills_and_proficiencies, name='skills_and_proficiencies'),
]
