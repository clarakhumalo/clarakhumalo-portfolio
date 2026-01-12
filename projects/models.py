from django.db import models

# Create your models here.

class Project(models.Model):
  name = models.CharField(max_length=255)
  video = models.FileField(upload_to='assets/videos/')
  tools = models.CharField(max_length=255)
  skills = models.CharField(max_length=255)
  link = models.URLField(max_length=200)