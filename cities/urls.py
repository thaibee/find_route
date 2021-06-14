from django.urls import path
from .views import CitiesList

urlpatterns = [
    path('', CitiesList.as_view(), name='cities_list')
]