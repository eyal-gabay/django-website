from django.urls import path

from . import views
from . import instaviews
from . import youtube
from . import workspace


urlpatterns = [
    path('', views.index, name='index'),
    path('index.php', views.index, name='index'),
    path('insta', instaviews.main, name='insta'),
    path('youtube/download', youtube.download_youtube_video_page, name='youtube'),
    path('workspace', workspace.workspace, name='workspace'),
    path('workspace.php', workspace.index, name='workspace index'),
]
