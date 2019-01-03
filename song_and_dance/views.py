from django.shortcuts import render, redirect

from .models import Song

import csv

# Create your views here.


def song_and_dance(request):
    return render(request, 'song_and_dance/song_and_dance.html', {})


def import_songs():
    with open("songs.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            style = line[0]
            name = line[1]
            url = line[2]
            notes = line[3]
            print(line)
            Song.objects.create(style=style, name=name, url=url, notes=notes)


def generate(request):
    playlist = None
    if request.GET:
        single_video_link = 'https://www.youtube.com/watch?v='
        playlist_link = 'http://www.youtube.com/watch_videos?video_ids='
        songs = []
        for style in Song.styles:
            if style[0] in request.GET:
                songs = songs + list(Song.objects.filter(style=style[0]))
        ids = [song.url.split(single_video_link)[1] for song in songs]
        playlist = playlist_link + ",".join(ids)
    if playlist:
        return render(request, 'song_and_dance/song_and_dance.html', {'playlist': playlist})
    else:
        return redirect('song_and_dance')
