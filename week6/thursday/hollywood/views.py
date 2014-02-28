# Create your views here.
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hollywood.forms import MovieForm
from hollywood.models import Movie, Actor


def home(request):
    return render(request, "home.html")

def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies/movies.html", {'movies': movies})

def new_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/movies")
    else:
        form = MovieForm()
    data = {'form': form}
    return render(request, "movies/new_movie.html", data)

def view_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = {"movie": movie}
    return render(request, "movies/view_movie.html", data)

def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            if form.save():
                return redirect("/movies/{}".format(movie_id))
    else:
        form = MovieForm(instance=movie)
    data = {"movie": movie, "form": form}
    return render(request, "movies/edit_movie.html", data)

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("/movies")

def actors(request):
    actors = Actor.objects.all()
    return render(request, "actors/actors.html", {'actors': actors})


def ajaxiness(request):
    return HttpResponse("hello")

def more_information(request):
    data = {"info": "baylee is cool"}
    return render(request, "more_information.html", data)