from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cities.forms import CitiesForm
from cities.models import Cities


class CitiesList(ListView):
    model = Cities

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            form = CitiesForm(self.request.POST)
        else:
            form = CitiesForm()
        context['form'] = form
        return context


class CityDetail(DetailView):
    model = Cities
