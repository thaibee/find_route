from django.shortcuts import render
from django.views.generic import ListView
from cities.models import Cities


class CitiesList(ListView):
    model = Cities
