from django.contrib import admin
from trains.models import Train


@admin.register(Train)
class AdminTrain(admin.ModelAdmin):
    list_display = ['number_train', 'city_from', 'city_to', 'travel_time']
    list_editable = ['travel_time']
