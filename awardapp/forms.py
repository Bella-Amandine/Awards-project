from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Rating

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=40)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user', 'project']