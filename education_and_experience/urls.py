from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_and_experience, name='education_and_experience'),
]
