from .forms import NewMovieForm
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import random
from tmdbv3api import TMDb
from tmdbv3api import Movie, Discover, Genre
from . import api

#t3leport
# Create your views here.


def listView(request):
    if 'movies' not in request.session:
        request.session['movies'] = []

    return render(request, 'myapp/list.html', {
        'movies': request.session['movies']
    })

def addMovie(request):
    if request.method == 'POST':
        form = NewMovieForm(request.POST or None)
        if form.is_valid():
            movie = form.cleaned_data['movie']
            request.session['movies'] += [movie]
            return HttpResponseRedirect(reverse('myapp:list'))
        else:
            return render(request, 'myapp/add.html', {'form': form})

    return render(request, 'myapp/add.html', {
        'form': NewMovieForm(),
    })

def randomMovie(request):
    if request.method == 'POST':
        movie = random.choice(request.session['movies'])
        print('--->',movie)
        return render(request, 'myapp/random.html', {'movie': movie})
    return render(request, 'myapp/random.html')


def selectMovie(request):
    tmdb = TMDb()

    key = '7d6216389a32b10277a26cdf348a9f68'
    tmdb.api_key = key
    tmdb.language = 'en'
    tmdb.debug = True
    
    my_movie = Movie()
    titles = []
    overview = []
    
    recommendations = my_movie.recommendations(movie_id=100)
    for r in recommendations:
        titles.append(r.title)
        overview.append(r.overview)
    data = zip(titles,overview)

    print('--> END')

    return render(request, 'myapp/movies.html', {'movies': data})

def discoverMovie(request):
    discover = Discover()
    movie = discover.discover_movies({
        'with_genres': 'adventure',
    })
    return render(request, 'myapp/discover.html', {'movie':movie})

def popularMovie(request):
    movie = Movie()
    popular = movie.popular()
    data = []
    for p in popular:
        data.append('id ' + str(p.id))
        data.append('title ' +p.title)
        data.append('overview ' + p.overview)
        data.append('path ' + p.poster_path)

    return render(request, 'myapp/popular.html', {'data': data})
    