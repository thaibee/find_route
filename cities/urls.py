from django.urls import path
from .views import CitiesList, CityDetail, CityAdd, CityUpdate, CityDelete

urlpatterns = (
    path('', CitiesList.as_view(), name='home'),
    path('city/<int:pk>', CityDetail.as_view(), name='city'),
    path('update/<int:pk>', CityUpdate.as_view(), name='update'),
    path('delete/<int:pk>', CityDelete.as_view(), name='delete'),
    path('add/', CityAdd.as_view(), name='add'),
)
