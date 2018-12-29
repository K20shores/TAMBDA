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
from .views import home, lessons, competitions, performance_team, song_and_dance

urlpatterns = [
    path('', include('accounts.urls')),
    path('', home, name='home'),
    path('lessons/', lessons, name='lessons'),
    path('competitions/', competitions, name='competitions'),
    path('performance_team/', performance_team, name='performance_team'),
    path('song_and_dance/', song_and_dance, name='song_and_dance'),
    path('admin/', admin.site.urls),
]
