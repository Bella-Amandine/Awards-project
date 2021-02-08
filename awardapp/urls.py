from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('', views.index, name = 'index'),
    path('post/project/', views.postProject, name = 'post'),
    path('rate/project/<project_id>', views.rate_project, name = 'rate'),
    path('project/<project_id>', views.get_single_project, name = 'project')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)