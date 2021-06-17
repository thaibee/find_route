from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cities.forms import CityForm
from cities.models import City


class CitiesList(ListView):
    model = City
    form = CityForm()
    template_name = 'cities/home.html'
    paginate_by = 10


class CityDetail(DetailView):
    model = City


class CityAdd(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/add.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан'


class CityUpdate(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно обновлен'


class CityDelete(SuccessMessageMixin, DeleteView):
    model = City
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):  # удаление без подтверждения.
        city_name = City.objects.filter(id=self.kwargs['pk'])[0]
        messages.success(request, f'Город {city_name} удален')
        return self.post(self, request, *args, **kwargs)
