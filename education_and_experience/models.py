from django.db import models

class EducationAndExperience(models.Model):
  field_or_occupation = models.CharField(max_length=255)
  company_or_institution = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  duration = models.CharField(max_length=255)