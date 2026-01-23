from os import path
import os
from django.db import models

import projects

class Project(models.Model):
  name = models.CharField(max_length=255)
  video = models.FileField(upload_to='videos/')
  tools = models.CharField(max_length=255)
  skills = models.CharField(max_length=255)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"{self.name} Project"
  

for v in Project.objects.all():
  if v.video.name.startswith('videos/'):
    v.video.name = f'videos/{v.video.name}'
    v.save(update_fields=['video'])
    print(f"Fixed video path for project: {v.name}")