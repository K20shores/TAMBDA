from django.shortcuts import render

# Create your views here.

def song_and_dance(request):
    return render(request, 'song_and_dance/song_and_dance.html', {})

def generate(request):
    if request.GET:
        print(request.GET['foxtrot'])
        print(request.GET['waltz'])
    return render(request, 'song_and_dance/song_and_dance.html', {})