from django import forms
from cities.models import Cities


class CitiesForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города',
    }))

    class Meta:
        model = Cities
        fields = ('name',)
