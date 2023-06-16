from django.contrib.gis.db import models as geomodels
from django.db import models
from apps.users.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='fields/')

    def __str__(self):
        return self.image.name


class Field(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    images = models.ManyToManyField(Image, related_name='fields', null=True, blank=True)
    price_per_hour = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = geomodels.PointField()

    def __str__(self):
        return self.name



