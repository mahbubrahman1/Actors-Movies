from django.urls import path
from FilmIndustry import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addmovie/', views.add_movie, name='add_movie'),
    path('addactor/', views.add_actor, name='add_actor'),
    path('movies/<int:a_id>/', views.movies, name='movies'),
    path('editactor/<int:a_id>/', views.edit_actor, name='edit_actor'),
]