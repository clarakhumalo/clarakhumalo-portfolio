from django.db import models

class AboutMe(models.Model):
  name = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  image = models.FileField(upload_to='assets/images/')
  description = models.CharField(max_length=255)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"About {self.name}"

# from about_me.models import AboutMe
# AboutMe.objects.all()
# about_me.save()
# description_lines = description="""I’m an early-career software developer who loves learning new technologies and building projects that help me grow. I have experience with programming fundamentals, web development, and tools like GitHub, and I'm constantly expanding my skills through self-driven projects and coursework.
# I focus on writing clean, simple code and breaking down complex problems into manageable steps. My portfolio reflects my learning journey — each project represents something new I’ve learned or a challenge I’ve overcome."""
# about_me = AboutMe(name='Clara Khumalo', title='Software Developer', image=r'about_me\assets\images\clara-khumalo.jpg', description=description_lines , link=r'https://github.com/clarakhumalo')