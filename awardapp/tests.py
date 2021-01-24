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

