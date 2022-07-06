from atexit import register
from django.contrib import admin
from FilmIndustry.models import Actor, Movie

admin.site.register(Actor)
admin.site.register(Movie)

# username = admin
# password = admin
