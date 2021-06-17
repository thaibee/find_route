from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainsList.as_view(), name='home'),
    path('update/<int:pk>', views.TrainUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.TrainDelete.as_view(), name='delete'),
    path('add/', views.TrainAdd.as_view(), name='add'),
]
