from django.db import models

class Socials(models.Model):
  platform_name = models.CharField(max_length=255)
  image = models.FileField(upload_to='assets/images/')
  profile_link = models.URLField(max_length=200)
  social_username = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.platform_name} - {self.social_username}"

# from socials.models import Socials
# Socials.objects.all()
# social.save()
# social = Socials(platform_name='LinkedIn', image=r'socials\assets\images\linkedin-profile-image.png', profile_link=r'www.linkedin.com/in/clara-juana-khumalo', social_username='clara-juana-khumalo')
# social = Socials(platform_name='Gmail', image=r'socials\assets\images\email-profile-image.png', profile_link=r'mailto:clarakhumalo14@gmail.com', social_username='clarakhumalo14@gmail.com')