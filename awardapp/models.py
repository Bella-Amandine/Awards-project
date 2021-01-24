from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profiles/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length = 255)

class Project(models.Model):
    project_title = models.CharField(max_length = 255)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to = 'projects/')
    project_link = models.CharField(max_length = 255)