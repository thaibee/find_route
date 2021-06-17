from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    number_train = models.CharField(max_length=30, unique=True, verbose_name='Номер поезда')
    travel_time = models.SmallIntegerField(verbose_name='Время в пути')
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_from_set', verbose_name='Из города')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_to_set', verbose_name='В город')

    def __str__(self):
        return self.number_train + ' Из города ' + self.city_from.name + ' в ' + self.city_to.name

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'

    def clean(self):
        if self.city_to == self.city_from:
            raise ValidationError('Города должны быть разные')
        qs = Train.objects.filter(
            city_from=self.city_from,
            city_to=self.city_to,
            travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Такой маршрут уже есть')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
