from django import forms
from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города',
    }))

    class Meta:
        model = City
        fields = ('name',)
