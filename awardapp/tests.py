from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating

# Create your tests here.
class ProfileTestCase(TestCase):

    def setUp(self):
        self.new_user = User(username = "amandine")
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user, profile_picture = 'default.jpg', bio = "bla bla blaaa", contact = "0782927483")

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_create_profile_method(self):
        self.new_profile.create_profile()
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile_method(self):
        self.new_profile.create_profile()
        self.new_profile.delete_profile()
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) == 0)

class ProjectTestCase(TestCase):
    def setUp(self):
        self.new_user = User(username = "amandine")
        self.new_user.save()

        self.new_profile = Profile(user = self.new_user, profile_picture = 'default.jpg', bio = "bla bla blaaa", contact = "0782927483")
        self.new_profile.create_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()

    def test_create_project_method(self):
        self.new_project = Project(owner = self.new_profile, project_title = "Awards", project_description ="bla blahi eereu", project_image = "default.jpg", project_link = "https://github.com")
        self.new_project.create_project()
        projects = Project.get_all_projects()
        self.assertTrue(len(projects) > 0)

    def test_get_all_projects_method(self):
        self.new_project = Project(owner = self.new_profile, project_title = "Awards", project_description ="bla blahi eereu", project_image = "default.jpg", project_link = "https://github.com")
        self.new_project.create_project()

        self.new_project1 = Project(owner = self.new_profile, project_title = "Akan", project_description ="bla blahi eereu", project_image = "default.jpg", project_link = "https://github.com")
        self.new_project1.create_project()

        projects = Project.get_all_projects()
        self.assertEqual(len(projects), 2)

    def test_get_project_by_id_method(self):
        self.new_project = Project(owner = self.new_profile, project_title = "Awards", project_description ="bla blahi eereu", project_image = "default.jpg", project_link = "https://github.com")
        self.new_project.create_project()

        self.new_project1 = Project(owner = self.new_profile, project_title = "Akan", project_description ="bla blahi eereu", project_image = "default.jpg", project_link = "https://github.com")
        self.new_project1.create_project()

        project = Project.get_project_by_id(self.new_project1.id)
        self.assertEqual(self.new_project1.project_title, "Akan")
