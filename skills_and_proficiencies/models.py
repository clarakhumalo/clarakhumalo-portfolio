from django.db import models

class SkillsAndProficiencies(models.Model):
  skill = models.CharField(max_length=255)
  extras = models.CharField(max_length=255)
  skill_percentage = models.IntegerField()

  def __str__(self):
    return f"{self.skill} Skill"