from django.db import models

class EducationAndExperience(models.Model):
  field_or_occupation = models.CharField(max_length=255)
  company_or_institution = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  duration = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.field_or_occupation} at {self.company_or_institution}"

# from education_and_experience.models import EducationAndExperience
# EducationAndExperience.objects.all()
# education_and_experience.save()
# education_and_experience = EducationAndExperience(field_or_occupation='Bsc Computer science, part-time studies', company_or_institution='University of The People', description='Successfully built an E-Commerce System, Simple Clock Application, Generic Library Catalog,  Online Chat Application, and Weather Information App using Java and Java FX.', duration='PRESENT')
# education_and_experience = EducationAndExperience(field_or_occupation='Independent Coding Tutor', company_or_institution='Cheery Robot Academy', description='Provided direction for game development.', duration='2024 - 2025')
# education_and_experience = EducationAndExperience(field_or_occupation='Private Programming Tutor', company_or_institution='Superprof', description='Gave clear, supportive guidance that received excellent ratings and ranked as an ambassador, displaying outstanding technical ability and communication skills.', duration='2023 - PRESENT')
# education_and_experience = EducationAndExperience(field_or_occupation='National Certification in Software Engineering', company_or_institution='WeThinkCode', description='Completed various projects in the following modules: Programming Fundamentals, Object-Oriented Programming, Brownfield Software Development, Client-side Web Applications, and Mobile Application Development.', duration='2022 - 2023')