from django.db import models

class Socials(models.Model):
  platform_name = models.CharField(max_length=255)
  image = models.FileField(upload_to='assets/images/')
  profile_link = models.URLField(max_length=200)
  social_username = models.CharField(max_length=255)