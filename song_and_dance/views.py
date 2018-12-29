from django.shortcuts import render

# Create your views here.

def song_and_dance(request):
    return render(request, 'song_and_dance/song_and_dance.html', {})