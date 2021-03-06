from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import movie


# Create your views here.


def index(request):
    movies = movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def detail(request, movie_id):
    movie1 = get_object_or_404(movie, id=movie_id)
    return render(request, "movies/detail.html", {"movie": movie1})
