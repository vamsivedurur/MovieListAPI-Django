
from django.contrib import admin
from django.urls import path

from watchlist_app.views import Movie_detail, Movie_list

urlpatterns = [
    path('list/', Movie_list,name='movie_list'),
    path('list/<int:pk>',Movie_detail,name='movie_detail'),
]
