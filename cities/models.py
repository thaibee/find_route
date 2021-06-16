from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

