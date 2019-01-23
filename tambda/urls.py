"""tambda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
import social_django as social_django

urlpatterns = [
    path('', include('accounts.urls')),
    path('song_and_dance/', include('song_and_dance.urls')),
    path('lessons/', views.lessons, name='lessons'),
    path('competitions/', views.competition_home, name='competition_home'),
    path('competitions/attire', views.competition_attire, name='competition_attire'),
    path('competitions/packing_list', views.competition_packing_list, name='competition_packing_list'),
    path('competitions/pictures', views.competition_pictures, name='competition_pictures'),
    path('competitions/results', views.competition_results, name='competition_results'),
    path('competitions/forms', views.competition_forms, name='competition_forms'),
    path('competitions/syllabus', views.competition_syllabus, name='competition_syllabus'),
    path('competitions/links', views.competition_links, name='competition_links'),
    path('performance_team/', views.performance_team, name='performance_team'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('officers/', views.officers, name='officers'),
    path('privacy/', views.privacy, name='privacy'),
    path('consent/', views.consent, name='consent'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls'), name='social'),
#    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
]
