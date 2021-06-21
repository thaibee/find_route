from django import forms
from cities.models import City
from routes.models import Route


class RouteForm(forms.Form):

    city_from = forms.ModelChoiceField(label='Из',
                                       queryset=City.objects.all(),
                                       widget=forms.Select(attrs={
                                           'class': 'form-control js-example-basic-single',
                                       }))
    city_to = forms.ModelChoiceField(label='В',
                                     queryset=City.objects.all(),
                                     widget=forms.Select(attrs={
                                         'class': 'form-control js-example-basic-single',
                                     }))
    cities = forms.ModelMultipleChoiceField(label='через',
                                            queryset=City.objects.all(),
                                            required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control js-example-basic-multiple'
                                            }))
    road_time = forms.IntegerField(label='Время в пути(часы)',
                                   widget=forms.NumberInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Время в пути',
                                   }))
