from django.shortcuts import render

def home(request):
    return render(request, 'tambda/home.html', {})

def lessons(request):
    return render(request, 'tambda/lessons.html', {})

def competitions(request):
    return render(request, 'tambda/competitions.html', {})

def performance_team(request):
    return render(request, 'tambda/performance_team.html', {})