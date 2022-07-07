from django.shortcuts import render
from django.http import HttpResponse
from FilmIndustry.models import Actor, Movie
from FilmIndustry import forms


# homepage
def home(request):
    actors = Actor.objects.all()

    return render(request, 'film_industry/home.html', {'actors': actors})


# movie list 
def movies(request, a_id):
    actor = Actor.objects.get(pk=a_id)
    movies = Movie.objects.filter(actor=a_id)

    return render(request, 'film_industry/movies.html', {'actor': actor, 'movies': movies})


# add actor form 
def add_actor(request):
    form = forms.ActorForm()

    if request.method == 'POST':
        form = forms.ActorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.ActorForm()

    return render(request, 'film_industry/add_actor.html', {'a_form': form})


# add movie form 
def add_movie(request):
    form = forms.MovieForm()

    if request.method == 'POST':
        form = forms.MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.MovieForm()

    return render(request, 'film_industry/add_movie.html', {'m_form': form})


# edit actor
def edit_actor(request, a_id):
    actor = Actor.objects.get(pk=a_id)
    form = forms.ActorForm(instance=actor)
    
    return render(request, 'film_industry/edit_actor.html', {'a_form': form})