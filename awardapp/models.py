from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profiles/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length = 255)