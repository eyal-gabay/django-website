from django.urls import path

from . import views
from . import notes

urlpatterns = [
    # path('', views.index, name='index'),
    path('notes', notes.main, name='index'),
]

