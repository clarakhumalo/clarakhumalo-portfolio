from django.db import models

class SkillsAndProficiencies(models.Model):
  skill = models.CharField(max_length=255)
  extras = models.CharField(max_length=255)
  skill_percentage = models.IntegerField()
  hover = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.skill} Skill"

# from skills_and_proficiencies.models import SkillsAndProficiencies
# SkillsAndProficiencies.objects.all()
# skills_and_proficiencies.save()
# skillsandproficiency = SkillsAndProficiencies(skill='Python', extras='Advanced skills such as API Integration, Unittesting, and more', skill_percentage='90', hover='Estimated Python proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='Java', extras='Advanced skills such as API Integration, JUnit, and more', skill_percentage='93', hover='Estimated Java proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='C#', extras='Skills such as Windows Forms and more', skill_percentage='87', hover='Estimated C# proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='Web Development', extras='HTML, CSS, JavaScript, Django & React', skill_percentage='97', hover='Estimated Web Development proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='Database Management', extras='SQL & SQLite', skill_percentage='93', hover='Estimated Database Management proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='Docker', extras='', skill_percentage='83', hover='Estimated Docker proficiency')
# skillsandproficiency = SkillsAndProficiencies(skill='Git', extras='Branching, Merging, Commits etc.', skill_percentage='97', hover='Estimated Git proficiency')
