from django.db import models

class Skills_And_Proficiencies(models.Model):
  skill = models.CharField(max_length=255)
  extras = models.CharField(max_length=255)
  skill_percentage = models.IntegerField()