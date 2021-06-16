from django.forms import ModelForm
from cities.models import Cities


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['name']
