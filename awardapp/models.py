from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profiles/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length = 255)

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    project_title = models.CharField(max_length = 255)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to = 'projects/')
    project_link = models.CharField(max_length = 255)

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratings')
    comment = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    design_rate = models.IntegerField(default= 0)
    usability_rate = models.IntegerField(default= 0)
    content_rate = models.IntegerField(default= 0)
