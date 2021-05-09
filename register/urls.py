from django.urls import path

from . import views

urlpatterns = [
    path('re', views.re, name='index'),
    path('', views.index, name='index'),
    path('logout', views.log_out, name='log_out')
]
