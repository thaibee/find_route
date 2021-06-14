from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Cities)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


