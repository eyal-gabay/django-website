from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
import pafy


def download_youtube_video_page(request):
    try:
        path = request.GET["download"]
        try:
            video = pafy.new(path)
        except ValueError:
            return render(request, "root/youtube/download.html")
        os.system("rm database/songs/song.webm")
        video.audiostreams[3].download(filepath="database/songs/song.webm")
        file_path = os.path.join(settings.MEDIA_ROOT, "database/songs/song.mp3")
        os.system('ffmpeg -i "/home/eyal/PycharmProjects/python/oauth2/database/songs/song.webm" -vn -ab 128k -ar 44100\
                  -y "/home/eyal/PycharmProjects/python/oauth2/database/songs/song.mp3";')
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    except MultiValueDictKeyError:
        return render(request, "root/youtube/download.html")
