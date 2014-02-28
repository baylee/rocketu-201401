from django.forms import ModelForm
from hollywood.models import Movie

__author__ = 'baylee'


class MovieForm(ModelForm):
    class Meta:
        model = Movie