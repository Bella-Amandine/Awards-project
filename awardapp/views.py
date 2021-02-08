from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProjectForm, RatingForm
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


def index(request):

    default_projects = Project.objects.filter(owner = request.user.profile.id).all()
    all_project = Project.get_all_projects()

    if default_projects:
        random_project = random.choice(default_projects)  
    else:
        random_project = random.choice(all_project)

    return render(request, 'award/index.html', {'my_project': random_project, 'projects': all_project})

@login_required(login_url='login')
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

def get_single_project(request, project_id):
    project = Project.get_project_by_id(project_id)
    ratings = Rating.get_ratings_by_project(project_id)
   
    return render(request, 'award/single-project.html', {'project': project, 'ratings': ratings})

@login_required(login_url='login')
def rate_project(request, project_id):
    if request.method =='POST':
        form = RatingForm(request.POST)
        if form.is_valid():

            new_rate = form.save(commit=False)
            user = request.user.profile
            project = Project.get_project_by_id(project_id)

            new_rate.user = user
            new_rate.project = project
            new_rate.save()

            # go to single project
            return redirect('index')
    else:
        form = RatingForm()
        return render(request, 'award/rate-form.html', {'form': form})



