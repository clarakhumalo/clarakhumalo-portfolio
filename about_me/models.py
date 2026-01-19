from django.db import models

class AboutMe(models.Model):
  name = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  image = models.FileField(upload_to='images/')
  description = models.CharField(max_length=730)
  link = models.URLField(max_length=200)

  def __str__(self):
    return f"About {self.name}"

# from about_me.models import AboutMe
# import os
# AboutMe.objects.all()
# about_me.save()
# description_lines = """I’m an early-career software developer who loves learning new technologies and building projects that help me grow. I have experience with programming fundamentals, web development, and tools like GitHub, and I'm constantly expanding my skills through self-driven projects and coursework.
# I focus on writing clean, simple code and breaking down complex problems into manageable steps. My portfolio reflects my learning journey — each project represents something new I’ve learned or a challenge I’ve overcome."""
# about_me = AboutMe(name='Clara Khumalo', title='Software Developer', image=r'images\clara-khumalo.jpg', description=description_lines , link=r'https://github.com/clarakhumalo')

# for aboutme in AboutMe.objects.all():
#     filename = os.path.basename(aboutme.image.name)
#     print(filename)
#     aboutme.image = f'media/images/{filename}'
#     print(aboutme.image)
#     aboutme.save(update_fields=['image'])


# about_me = AboutMe.objects.first()
# about_me.image.path     # absolute path
# about_me.image.url      # /media/images/xxx.jpg
# about_me.image.size     # > 0