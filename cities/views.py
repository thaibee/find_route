from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cities.forms import CitiesForm
from cities.models import Cities


class CitiesList(ListView):
    model = Cities
    form = CitiesForm()
    template_name = 'cities/cities_list.html'
    paginate_by = 10


class CityDetail(DetailView):
    model = Cities


class CityAdd(SuccessMessageMixin, CreateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'cities/cities_add.html'
    success_url = reverse_lazy('cities_list')
    success_message = 'Город успешно создан'


class CityUpdate(SuccessMessageMixin, UpdateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'cities/cities_update.html'
    success_url = reverse_lazy('cities_list')
    success_message = 'Город успешно обновлен'


class CityDelete(SuccessMessageMixin, DeleteView):
    model = Cities
    success_url = reverse_lazy('cities_list')

    def get(self, request, *args, **kwargs):  # удаление без подтверждения.
        city_name = Cities.objects.filter(id=self.kwargs['pk'])[0]
        messages.success(request, f'Город {city_name} удален')
        return self.post(self, request, *args, **kwargs)
