from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('', views.index, name = 'index'),
    path('post/project/', views.postProject, name = 'post')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)