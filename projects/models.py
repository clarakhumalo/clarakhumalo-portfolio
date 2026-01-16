from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=255)
  video = models.FileField(upload_to='assets/videos/')
  tools = models.CharField(max_length=255)
  skills = models.CharField(max_length=255)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"{self.name} Project"