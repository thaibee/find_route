from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from trains.forms import TrainForm
from trains.models import Train


class TrainsList(ListView):
    model = Train
    template_name = 'trains/home.html'


class TrainAdd(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/add.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Маршрут успешно создан'


class TrainUpdate(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Маршрут обновлен'


class TrainDelete(SuccessMessageMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):  # удаление без подтверждения.
        train_name = Train.objects.filter(id=self.kwargs['pk'])[0]
        messages.success(request, f'Маршрут {train_name} удален')
        return self.post(self, request, *args, **kwargs)
