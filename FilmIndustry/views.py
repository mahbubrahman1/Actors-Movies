from django.shortcuts import render
from django.http import HttpResponse
from FilmIndustry.models import Actor, Movie
from FilmIndustry import forms


def home(request):
    actors = Actor.objects.all()

    return render(request, 'film_industry/home.html', {'actors': actors})

def movies(request):
    return render(request, 'film_industry/movies.html')

def add_actor(request):
    form = forms.ActorForm()

    if request.method == 'POST':
        form = forms.ActorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.ActorForm()

    return render(request, 'film_industry/add_actor.html', {'a_form': form})

def add_movie(request):
    form = forms.MovieForm()

    if request.method == 'POST':
        form = forms.MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.MovieForm()

    return render(request, 'film_industry/add_movie.html', {'m_form': form})
