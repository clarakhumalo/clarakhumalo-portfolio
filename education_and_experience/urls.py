from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('education-and-experience/', views.education_and_experience, name='education_and_experience'),
]
