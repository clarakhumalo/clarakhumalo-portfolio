from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=255)
  video = models.FileField(upload_to='media/videos/')
  tools = models.CharField(max_length=255)
  skills = models.CharField(max_length=255)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"{self.name} Project"
  
# from projects.models import Project
# import os
# Project.objects.all()
# project.save()
# project = Project(name='Java Pomodoro Timer App', video=r'projects\assets\videos\java-pomodoro-timer-app-clip.mp4', tools='Visual Studio Code, GitHub', skills='Java, JavaFX, SceneBuilder, Version Control', link=r'https://github.com/clarakhumalo/PomodoroTimerApp')
# project = Project(name='Web Pomodoro Timer', video=r'projects\assets\videos\web-pomodoro-timer-app-clip.mp4', tools='Visual Studio Code, GitHub', skills='HTML, CSS, JavaScript, Git Version Control', link=r'https://github.com/clarakhumalo/WebPomodoro')
# project = Project(name='Portfolio Website V1', video=r'projects\assets\videos\portfolio-website-v1-clip.mp4', tools='Visual Studio Code, GitHub', skills='HTML, CSS, JavaScript, Git Version Control', link=r'https://github.com/clarakhumalo/clara-khumalo-web-portfolio')
# project = Project(name='Professional Portfolio Website', video=r'projects\assets\videos\professional-portfolio-website-clip.mp4', tools='Visual Studio Code, GitHub', skills='HTML, CSS, JavaScript, Git Version Control, Django', link=r'https://github.com/clarakhumalo/clarakhumalo-portfolio')
# project = Project(name='Java Coding Tutorials App', video=r'projects\assets\videos\java-coding-tutorials-app-clip.mp4', tools='Visual Studio Code, GitHub', skills='Java, JavaFX, SceneBuilder, Git Version Control', link=r'https://github.com/clarakhumalo/JavaCodingTutorialsApp')
# project = Project(name='Python Coding Tutorials App', video=r'projects\assets\videos\python-coding-tutorials-app-clip.mp4', tools='Visual Studio Code, GitHub', skills='Python, Git Version Control', link=r'https://github.com/clarakhumalo/PythonCodingTutorialsApp')
# project = Project(name='Gratitude Journal', video=r'projects\assets\videos\gratitude-journal-clip.mp4', tools='Visual Studio Code, GitHub', skills='HTML, CSS, JavaScript, Django, Git Version Control', link=r'https://github.com/clarakhumalo/GratitudeJournal')


# for project in Project.objects.all():
#     filename = os.path.basename(project.video.name)
#     print(filename)
#     project.video = f'media/videos/{filename}'
#     print(project.video)
#     project.save(update_fields=['video'])