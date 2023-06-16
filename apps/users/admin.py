from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from apps.users.models import User


@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ('phone_number', 'location', 'username', 'email')


