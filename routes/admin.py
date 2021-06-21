from django.contrib import admin
from .models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'city_from', 'city_to', 'road_time']