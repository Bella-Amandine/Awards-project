from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProjectForm
from .models import Profile, Project, Rating
import random

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            new_profile = Profile(user = new_user)
            new_profile.create_profile()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {"form":form})

@login_required(login_url='login')
def index(request):
    print(request.user.profile.id)

    default_projects = Project.objects.filter(owner = request.user.profile.id).all()
    

    if len(default_projects) == 0:
        print('you have not yet posted a projects')
    else:
        print('you have already posted')

    return render(request, 'award/index.html')

def postProject(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():

            new_project = form.save(commit=False)
            owner = request.user.profile

            new_project.owner = owner
            new_project.save()

            return redirect('index')

    else:
        form = ProjectForm()
        return render(request, 'award/post-project.html', {"form": form})
