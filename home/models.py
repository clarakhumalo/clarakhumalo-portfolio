from django.db import models

class Home(models.Model):
    myname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    github_profile_link = models.URLField(max_length=200)
    linkedin_profile_link = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.myname} - {self.title}"