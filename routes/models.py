from django.db import models
from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название маршрута')
    road_time = models.SmallIntegerField(verbose_name='Общее время в пути')
    city_from = models.ForeignKey(City,
                                  on_delete=models.CASCADE,
                                  verbose_name='Из какого города',
                                  related_name='route_from',
                                  )
    city_to = models.ForeignKey(City,
                                on_delete=models.CASCADE,
                                verbose_name='В какой город',
                                related_name='route_to',)
    trains = models.ManyToManyField(Train, verbose_name='Список поездов')
