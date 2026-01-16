from django.db import models

class EducationAndExperience(models.Model):
  field_or_occupation = models.CharField(max_length=255)
  company_or_institution = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  duration = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.field_or_occupation} at {self.company_or_institution}"


# education_and_experience = EducationAndExperience(field_or_occupation='Bsc Computer science, part-time studies', company_or_institution='University of The People', description='Successfully built an E-Commerce System, Simple Clock Application, Generic Library Catalog,  Online Chat Application, and Weather Information App using Java and Java FX.', duration='PRESENT')