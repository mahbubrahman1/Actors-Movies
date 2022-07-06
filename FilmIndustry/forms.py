from dataclasses import field, fields
from pyexpat import model
from django import forms
from FilmIndustry import models


class ActorForm(forms.ModelForm):
    class Meta:
        model = models.Actor
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'nationality': forms.TextInput(attrs={'class':'form-control'}),
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = "__all__"
        widgets = {
            'release_date': forms.TextInput(attrs={'type':'date'})
        }