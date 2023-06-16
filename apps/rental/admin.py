from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from apps.rental.models import Field, Reservation

# admin.site.register(Field)
admin.site.register(Reservation)


@admin.register(Field)
class FieldAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'contact','address', 'price_per_hour', 'owner')
