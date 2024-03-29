from django.shortcuts import render

from watchlist_app.models import Movie

from django.http import JsonResponse

# Create your views here.

def Movie_list(request):
    movies=Movie.objects.all()
    data={'movies':list(movies.values())}
    return JsonResponse(data)

def Movie_detail(request,pk):
    movie=Movie.objects.get(pk=pk)
    data={'name':movie.name, 
          'description':movie.description,
          'active':movie.active
          }
    return JsonResponse(data)