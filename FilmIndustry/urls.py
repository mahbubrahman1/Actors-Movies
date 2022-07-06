from django.urls import path
from FilmIndustry import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addmovie', views.add_movie, name='add_movie'),
    path('addactor', views.add_actor, name='add_actor'),
]
