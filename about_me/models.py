from django.db import models

class AboutMe(models.Model):
  name = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  image = models.FileField(upload_to='assets/images/')
  description = models.CharField(max_length=255)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"About {self.name}"