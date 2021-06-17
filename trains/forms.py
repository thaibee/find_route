from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    number_train = forms.CharField(label='№', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя маршрута',
    }))
    travel_time = forms.CharField(label='Время в пути(часы)', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите время в пути',
    }))
    city_from = forms.ModelChoiceField(label='Из', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Выберите город',
    }))
    city_to = forms.ModelChoiceField(label='В', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Выберите город',
    }))

    class Meta:
        model = Train
        fields = '__all__'
