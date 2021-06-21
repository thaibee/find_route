from django.contrib import messages
from django.shortcuts import render, HttpResponse

from routes.forms import RouteForm
from routes.utils import get_route


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {
        'form': form
    })


def find_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                get_route(request, form)
                return render(request, 'routes/home.html', {
                    'form': form
                })
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {
                    'form': form
                })
        return render(request, 'routes/home.html', {
            'form': form
        })
    else:
        form = RouteForm()
        messages.warning(request, 'Введите данные')
        return render(request, 'routes/home.html', {
            'form': form
        })
