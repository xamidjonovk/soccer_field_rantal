from django.contrib.gis.db import models as geomodels
from django.db import models
from . import Field
from apps.users.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def total_cost(self):
        duration = self.end_time - self.start_time
        hours = duration.total_seconds() // 3600
        return hours * self.field.price_per_hour

    def __str__(self):
        return f'Reservation #{self.pk}'


