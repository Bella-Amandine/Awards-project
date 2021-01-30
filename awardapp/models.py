from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile', default = 0)
    profile_picture = models.ImageField(upload_to = 'profiles/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username} Profile'

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', default = 0)
    project_title = models.CharField(max_length = 255)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to = 'projects/')
    project_link = models.URLField()

    def __str__(self):
        return self.project_title

    def create_project(self):
        self.save()

    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_project_by_id(cls, id):
        return cls.objects.get(pk = id)

    def delete_projects(self):
        self.delete()


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratings')
    comment = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    design_rate = models.IntegerField(default= 0)
    usability_rate = models.IntegerField(default= 0)
    content_rate = models.IntegerField(default= 0)

    def __str__(self):
        return f'{self.project.project_title} Ratings'

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings_by_project(cls, project_id):
        return cls.objects.filter(project = project_id)
