from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from cities.forms import CitiesForm
from cities.models import Cities


class CitiesList(View):
    def get(self, request):
        model = Cities.objects.all()
        form = CitiesForm()
        return render(request, 'cities/cities_list.html', {'model': model, 'form': form})

    def post(self, request):
        model = Cities.objects.all()
        form = CitiesForm(request.POST)
        if form.is_valid():
            form.save()
            form = CitiesForm()
        print('post')
        return render(request, 'cities/cities_list.html', {'model': model, 'form': form})



class CityDetail(DetailView):
    model = Cities

class CityAdd(CreateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'cities/cities_add.html'
    success_url = reverse_lazy('cities_list')
