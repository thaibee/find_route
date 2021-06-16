from django.urls import path
from .views import CitiesList, CityDetail, CityAdd

urlpatterns = [
    path('', CitiesList.as_view(), name='cities_list'),
    path('city/<int:pk>', CityDetail.as_view(), name='city'),
    path('add/', CityAdd.as_view(), name='add'),
]