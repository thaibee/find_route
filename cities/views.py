from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cities.models import Cities


class CitiesList(ListView):
    model = Cities


class CityDetail(DetailView):
    model = Cities
